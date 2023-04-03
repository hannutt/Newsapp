from flask import Flask,request,url_for,redirect,flash
from flask import render_template
import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date, timedelta
import time
import random
from art import *
from calc import calc

from guestbook import guestbook
from covid import covid
from quiz import quiz
from webshop import webshop
from seeOrders import seeOrders
from login import login
from AddProduct import AddProduct
from chatbot import chatbot
from network import network
from charts import charts
from forget import forget
from ChangePsw import ChangePsw
from register import register
from calcBtn import calcBtn
from videoPlayer import videoPlayer
from imgView import imgView
from webshop2 import webshop2
from wdclone import wdclone
from textTranslate import textTranslate


import sqlite3
app = Flask(__name__)
app.register_blueprint(calc,url_prefix='')

app.register_blueprint(guestbook,url_prefix='')
app.register_blueprint(covid,url_prefix='')
app.register_blueprint(quiz,url_prefix='')
app.register_blueprint(webshop,url_prefix='')
app.register_blueprint(seeOrders,url_prefix='')
app.register_blueprint(login,url_prefix='')
app.register_blueprint(AddProduct,url_prefix='')
app.register_blueprint(chatbot,url_prefix='')
app.register_blueprint(network,url_prefix='')
app.register_blueprint(charts,url_prefix='')
app.register_blueprint(forget,url_prefix='')
app.register_blueprint(ChangePsw,url_prefix='')
app.register_blueprint(register,url_prefix='')
app.register_blueprint(calcBtn,url_prefix='')
app.register_blueprint(videoPlayer,url_prefix='')
app.register_blueprint(imgView,url_prefix='')
app.register_blueprint(webshop2,url_prefix='')
app.register_blueprint(wdclone,url_prefix='')
app.register_blueprint(textTranslate,url_prefix='')


app.secret_key = "key"


globresult=''
globcurrent =''
globend =''


@app.route('/')
def weather():
    global globcurrent
    currentdate = date.today()
    globcurrent = currentdate.strftime('%d.%m.%y')
   #formatDate = currentdate.strftime('%d.%m.%y')
   #lisätään 2 päivää tämänhetkiseen päivämäärään
    global globend
    endDate = currentdate + timedelta(days=2)
    globend = endDate.strftime('%d.%m.%y')
    page = requests.get('https://www.foreca.fi/finland/helsinki')
    soup = BeautifulSoup(page.text, 'html.parser')
    weather = soup.find('div', {'id':'obs_3d'})
   
    for weath in weather:
        
        result = weath.text
        #globaali muuttuja, että voidaan käyttää siihen talletettuja tietoja
        #saveweather funktiossa. muuttuja on alustettu funktion yläpuolella
        global globresult
        globresult = weath.text

    #funktiokutsu, näin voidaan käyttää useampaa funktiota samalla routella.
    weekNumberDayNum()

       
    #muuttuja var näytetään index.html:n varPlace kohdassa.
    return render_template('index.html',WeatherPlace=result,datetimePlace=globcurrent,datetimeEnd=globend,weekPlace=res,dayPlace=day)


def weekNumberDayNum():

    page = requests.get('https://www.viikkonumero.fi')
    soup = BeautifulSoup(page.text, 'html.parser')
    weeks = soup.find('span',{'id':'ugenr'})
    currentdate = datetime.datetime.now()
    global day
    day=currentdate.strftime("%j")

    for week in weeks:
        #globaali muuttuja että sitä voidaan käyttää weather funktion render templatessa
        global res
        res = week.text
        #korvataan tuloksen viikko sana tyhjillä merkeillä, eli saadaan ainoastaan viikon numero
        res = res.replace('Viikko','')
        



@app.route('/saveTxt',methods=['POST','GET'])
def saveWeather():
    currentdate = datetime.datetime.now()
    clocktime = currentdate.strftime('%d.%m.%y.%H.%M.%S')
    if request.method == 'POST':
        #lisätään tiedostonimeen pvm ja kellonaika sekuntien tarkkuudella
        f = open('weather'+clocktime+'.txt','x')
        f.write(globcurrent+' ')
        f.write('-')
        f.write(globend+' ')
        
        f.write(globresult)
        f.close()
        return render_template('success.html',Ad='Weather forecast saved!')

#reititys /stock
@app.route('/stock')

def stock():
    stocks = []
    page = requests.get('https://www.investing.com/indices/major-indices')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    result = soup.find(class_='datatable_body__3EPFZ')
   
    result2 = result.find_all('tr')
    for result in result2:
        finalresult = result.text
        #tallennetaan kaikki haettu data listaan
        stocks.append(result.text)
        #indexplace html-sivulla saa sisällöksi listan sisällön
    return render_template('stock.html',IndexPlace=stocks)


  
   
'''  if request.method == 'POST' and value=='True' and value2=='True':
        points = 2
        answer = 'Good'
        return render_template('quiz.html',answerPlace=answer,pointsPlace=points)
    
    elif value == 'False' or value2=='False':
        points = 1
        answer = 'Something went wrong!'
        return render_template('quiz.html',answerPlace=answer,pointsPlace=points)
    else:
        points = 0
        answer = 'Try again'
        return render_template('quiz.html',answerPlace=answer,pointsPlace=points) '''
        
    

#globaalimuuttuja että sitä ei tarvitse alustaa ja määritellä funktiossa joka uudelleen


if __name__ == '__main__':
    app.run(debug=True)