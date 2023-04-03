from flask import Flask, request, url_for, redirect, flash
from flask import render_template, Blueprint
import sqlite3

import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

forget= Blueprint('forget',__name__,static_folder='static',template_folder='templates')

@forget.route('/Forget')
def showPage():
    

    return render_template('forgetpsw.html')

@forget.route('/sendPsw',methods=['POST','GET'])

def forgetPsw():
    #globaali muuttuja, koska sitä käytetään myös sendMail funktiossa
    global mailAdd
    mailAdd = request.form['forgetmail']
    with sqlite3.connect('Flaskdb.db') as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.execute('SELECT email FROM LOGIN WHERE email=?',(mailAdd,))
            
            row = cursor.fetchone()
            if row:
                sendMail()

                return render_template('success.html',adPlace='Password sent to address '+mailAdd)

            else:
                return render_template('unsuccess.html',ad='Invalid email address!')




def sendMail():
    subject = "Your password!"
    body = "Password is testaaja"
    sender_email = "workapptest@yahoo.com"
    #receiver_email = "htuomela@gmail.com"
    password = "birnclvcfpfqscng"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = mailAdd
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, mailAdd,text)
                   