from flask import Flask, request, url_for, redirect, flash
from flask import render_template, Blueprint
from translate import Translator
import time
import datetime
from time import strftime
from datetime import date
import re

textTranslate = Blueprint('textTranslate', __name__,static_folder='static', template_folder='templates')

@textTranslate.route('/startTranslate')

def startTranslate():

    return render_template('textTranslate.html')

@textTranslate.route('/doTranslate',methods=['POST','GET'])
def doTrans():
    #regex laisekkeen kaava, etsitään vain numeroita
    digitspattern = '^[0-9]+$'
    #etsitään kirjaimia ja numeroita samasta lausekkeesta
    
    word = request.form['translateWord']
    toLn = request.form.get('toLang')
    #tarkistetaan regexillä löytyykö word muuttujasta kirjaimia ja numeroita
    digitresult = re.match(digitspattern,word)
    #translator= Translator(to_lang=toLn)
    #translation = translator.translate(word)

    #jos word on true, eli muuttujassa on numeroita ja kirjaimia
    if word.isdigit() == True:
        return render_template('textTranslate.html',wordPlace="Can't translate numbers!")
    elif word == '':
        return render_template('textTranslate.html',wordPlace='Please type a word')

    else:
        # timer eli lasketaan kuinka kauan käännöksen valmistumiseen menee aikaa.
        start_time = time.time()
        translator= Translator(to_lang=toLn)
        translation = translator.translate(word)
        end_time = time.time()
        elapsed_time = end_time - start_time
       
        #kuluneen ajan pyöristys round metodilla 2 desimaalin tarkkuuteen
        return render_template('textTranslate.html',lngPlace=toLn, wordPlace=translation,timePlace= round(elapsed_time,2))