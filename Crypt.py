from flask import Flask, request, url_for, redirect, flash,session
from flask import render_template, Blueprint
from cryptography.fernet import Fernet
import rsa
Crypt = Blueprint('Crypt', __name__,static_folder='static', template_folder='templates')

@Crypt.route('/cryptPage')
def cryptPage():
    return render_template('cryptText.html')

@Crypt.route('/startCrypting',methods=['POST','GET'])
def doEnCrypt():
    global privateKey
    publicKey, privateKey = rsa.newkeys(512)
    text = request.form['yourText']
    global encMessage
    encMessage = rsa.encrypt(text.encode(),publicKey)
    return render_template('cryptText.html',textPlace=encMessage)

       
    

@Crypt.route('/startDecrypting',methods =['POST','GET'])
def doDeCrypt():
     
     decMessage = rsa.decrypt(encMessage, privateKey).decode()
     return render_template('cryptText.html',detextPlace=decMessage)
    