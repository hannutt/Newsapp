from flask import Flask, request, url_for, redirect, flash,session
from flask import render_template, Blueprint
from cryptography.fernet import Fernet

Crypt = Blueprint('Crypt', __name__,static_folder='static', template_folder='templates')

@Crypt.route('/cryptPage')
def cryptPage():
    return render_template('cryptText.html')

@Crypt.route('/startCrypting',methods=['POST','GET'])
def doEnCrypt():
    text = request.form['yourText']
    key = Fernet.generate_key()
    fernet = Fernet(key)
    if request.form.get('EncBtn') == 'DoEnc':
        
        encMessage = fernet.encrypt(text.encode())
        decMessage = fernet.decrypt(encMessage).decode()
        return render_template('cryptText.html',textPlace=encMessage,keyPlace=key,detextPlace=decMessage)
    '''
    elif request.form.get('DecBtn') == 'DoDenc':
        #detext = request.form['message']
        decMessage = fernet.decrypt(encMessage).decode()
        return render_template('cryptText.html',detextPlace=decMessage)'''

'''
@Crypt.route('/startDecrypt',methods =['POST','GET'])
def doDeCrypt():
    detext = request.form['message']
    decMessage = fernet.decrypt(detext).decode()
    return render_template('cryptText.html',detextPlace=decMessage)'''