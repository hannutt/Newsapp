from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import sqlite3
import time
import datetime
from datetime import date
import requests
from bs4 import BeautifulSoup

covid = Blueprint('covid',__name__,static_folder='static',template_folder='templates')


@covid.route('/editCovid')
def EditCovid():
    return render_template('editCovid.html')
#reititys /covid
@covid.route('/covid')

def covid19():
    currentdate = datetime.datetime.now()
    formatDate = currentdate.strftime('%d.%m.%y')
    page2 = requests.get('https://www.worldometers.info/coronavirus/') 
    soup2 = BeautifulSoup(page2.text, 'html.parser')

    case = soup2.find(class_='maincounter-number')
    cases = case.find_all('span')

    for case in cases:
        covresult = case.text
        
    return render_template('covid.html',CovidPlace=covresult,covDate=formatDate,countryPlace='World')

#tartuntojen haku maittain funktioparametrin avulla covidBy on reititysosoite ja <c> parametri

@covid.route('/covidBy/<c>')

def covid19ByCountry(c):
    currentdate = datetime.datetime.now()
    formatDate = currentdate.strftime('%d.%m.%y')
    page2 = requests.get('https://www.worldometers.info/coronavirus/country/'+c)

    soup2 = BeautifulSoup(page2.text, 'html.parser')
   
    case = soup2.find(class_='maincounter-number')
    cases = case.find_all('span')

    for case in cases:
        covresult = case.text
    return render_template('covid.html',CovidPlace=covresult,covDate=formatDate,countryPlace=c.capitalize())

@covid.route('/', methods=["POST"])
#tulosten haku käyttäjän syötekenttään kirjoittamalla hakuehdolla

def covidByCountry():
    
    currentdate = datetime.datetime.now()
    formatDate = currentdate.strftime('%d.%m.%y')
    if request.method == "POST":
        c = request.form.get("countryName")
        page2 = requests.get('https://www.worldometers.info/coronavirus/country/'+c) 
        soup2 = BeautifulSoup(page2.text, 'html.parser')

        case = soup2.find(class_='maincounter-number')
        cases = case.find_all('span')

        for case in cases:
            covresult = case.text
           
            
        return render_template('covid.html',CovidPlace=covresult,covDate=formatDate,countryPlace=c.capitalize())

   
        
#savedatalla yhdistetään covid.html sivun lomake ja haluttu funktio news.py tiedostossa
@covid.route('/saveCovid',methods=['POST','GET'])
def saveData():
    if request.method == 'POST':
        # lomakkeen syötekenttien sisällön tallennus muuttujiin
        country = request.form['country']
        date = request.form['date']
        amount = request.form['amount']
        with sqlite3.connect('Flaskdb.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO COVID (country,date,amount) VALUES (?,?,?)',(country,date,amount))
            connection.commit()
        #funktion suorituksen / tallennuksen jälkeen näytetään success.html sivu ja data saved teksti
        return render_template('success.html',adPlace='Data saved')

@covid.route('/delCovid',methods=['POST','GET'])
def delCovidData():
    if request.method == 'POST':
        with sqlite3.connect('Flaskdb.db') as connection:
             cursor = connection.cursor()
             #delthis on piilotetun input kentän nimi, jonka kautta saadaan poistettava idnumero
             cursor.execute('DELETE FROM COVID WHERE idnum=?',[request.form['delthis']])
             connection.commit()
             return render_template('view.html')

@covid.route('/editCov', methods=['POST','GET'])
def editCovData():
    if request.method == 'POST':
         with sqlite3.connect('Flaskdb.db') as connection:
             connection.row_factory = sqlite3.Row
             cursor = connection.cursor()
             #editthis on piilotetun input kentän nimi, jossa on tietokannan id numero jonka kautta saadaan poistettava idnumero
             cursor.execute('SELECT idnum,country,amount,date FROM COVID WHERE idnum=?',[request.form['editthis']])
             rows = cursor.fetchall()
             connection.commit()
             return render_template('editCovid.html',rows=rows)

@covid.route('/updateCov',methods=['POST','GET'])
def updateCovData():
    if request.method == 'POST':
        with sqlite3.connect('Flaskdb.db') as connection:

            idnumb = request.form['updatethis']
            newDate = request.form['date']
            newCountry = request.form['country']
            newAmount = request.form['amount']
       
            cursor = connection.cursor()
            cursor.execute('UPDATE COVID SET country=?,date=?,amount=? WHERE idnum=?',(newCountry,newDate,newAmount,idnumb))
            connection.commit()
            return render_template('success.html',adPlace='Data edited')
            


@covid.route('/view')
def view():
    connection = sqlite3.connect('Flaskdb.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT idnum,country,date,amount FROM COVID')
    rows = cursor.fetchall()
    return render_template('view.html',rows=rows)
