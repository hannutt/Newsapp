from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import sqlite3
import time
import datetime
from datetime import date
import clipboard

guestbook = Blueprint('guestbook',__name__,static_folder='static',template_folder='templates')

#write.html sivun lataus ja kellonajan + päivämäärän lisääminen write.html sivuilla
#oleviin {{time}} ja {clocktime} kohtiin

@guestbook.route('/write')
def showWritePage():
    currentdate = datetime.datetime.now()
    dtime = currentdate.strftime('%d.%m.%y')
    clocktime = currentdate.strftime('%H:%M.%S')
    return render_template('guestbook.html',clockTime=clocktime,time=dtime)

#write.html sivun writeData lomakkeen tietojen tallennus
@guestbook.route('/writeData', methods=['POST','GET'])
def WriteData():
    #lista sanoista, joita ei hyväksytä
    swearwords = ['fuck','ass','idiot','nigga','moron','jerk','cunt','prick','crap','motherfucker','mother fucker']
    if request.method == 'POST':
        time = request.form['time']
        message = request.form['message']
        #muutetaan message kenttään syötetty teksti pienkiksi kirjaimiksi, koska listassa olevat kirosanat
        #ovat pienellä kirjoitettu. ilman muunnosta ohjelma ei löydä sanoja.
        message = message.lower()
        nickname = request.form['nickname']
     
        ctime = request.form['ctime']
        #tarkistus sisältääkö messagemuuttuja swearwords listalla olevia sanoja.
        result = any (Message in message for Message in swearwords)
        #jos muuttuja sisältää listassa olevia sanoja, palautetaan pelkästään unsuccess.html sivu
        #ja ad muuttujan teksti
        if result == True:
            return render_template('unsuccess.html',ad="We don't accept any swearwords!")
        #muussa tapauksessa tallennetaan viesti tietokantaan.
        else:

            with sqlite3.connect('Flaskdb.db') as connection:

                cursor = connection.cursor()
                cursor.execute('INSERT INTO GUESTBOOK (time,message,nickname,ctime) VALUES (?,?,?,?)', (time,message,nickname,ctime))
                connection.commit()
                return render_template('success.html')

@guestbook.route('/delMsg',methods=['POST','GET'])
def delMessage():
    if request.method == 'POST':
        with sqlite3.connect('Flaskdb.db') as connection:
             cursor = connection.cursor()
             #delthis on piilotetun input kentän nimi, jonka kautta saadaan poistettava idnumero
             cursor.execute('DELETE FROM GUESTBOOK WHERE idnum=?',[request.form['delmessage']])
             connection.commit()
             return render_template('success.html')




@guestbook.route("/showData", methods = ['POST','GET'])
def showData():
    
    connection = sqlite3.connect('Flaskdb.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT idnum,time,message,nickname,ctime FROM GUESTBOOK')
    global rows
    rows = cursor.fetchall()
    
    return render_template('guestbook.html',rows=rows)

@guestbook.route('/copyMsg', methods = ['POST','GET'])
def copyMessage():
    copymsg = request.form['copymessage']
    clipboard.copy(copymsg)

    return render_template('guestbook.html',rows=rows)
@guestbook.route('/searchData',methods=['POST','GET'])
def dbSearch():
    srcvalue = request.form['searchbox']
    if request.method == 'POST':
        with sqlite3.connect('Flaskdb.db') as connection:

            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            #sql haku nimimerkillä, ajankohdalla tai viestin sisällöllä. 3. srcvalue parametrin eteen ja taakse % merkit että LIKE hakuehto toimii
            cursor.execute('SELECT message FROM GUESTBOOK WHERE nickname=? OR time=? OR message LIKE ?',(srcvalue,srcvalue,'%'+srcvalue+'%'))
            searchrows = cursor.fetchall()
            if len(searchrows) == 0:
                return render_template('guestbook.html',rows=searchrows, nick='Nickname has not write anything')
            else:
                return render_template('guestbook.html',rows=searchrows, nick=srcvalue+' wrote')

@guestbook.route('/hideData', methods = ['POST','GET'])
def hideData():
    return render_template('guestbook.html')
        