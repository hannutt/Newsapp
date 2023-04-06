from flask import Flask, request, url_for, redirect, flash
from flask import render_template, Blueprint
from translate import Translator
import time
import datetime
from time import strftime
from datetime import date

textTranslate = Blueprint('textTranslate', __name__,static_folder='static', template_folder='templates')

@textTranslate.route('/startTranslate')

def startTranslate():

    return render_template('textTranslate.html')

@textTranslate.route('/doTranslate',methods=['POST','GET'])
def doTrans():
    word = request.form['translateWord']
    toLn = request.form.get('toLang')
    #translator= Translator(to_lang=toLn)
    #translation = translator.translate(word)

    
    if word == '':
        return render_template('textTranslate.html',wordPlace='Please type a word')
    elif StopIteration == True:
        return render_template('textTranslate.html',wordPlace='cant translate this')

    else:
        # timer eli lasketaan kuinka kauan käännöksen valmistumiseen menee aikaa.
        start_time = time.time()
        translator= Translator(to_lang=toLn)
        translation = translator.translate(word)
        end_time = time.time()
        elapsed_time = end_time - start_time
       
        #kuluneen ajan pyöristys round metodilla 2 desimaalin tarkkuuteen
        return render_template('textTranslate.html',lngPlace=toLn, wordPlace=translation,timePlace= round(elapsed_time,2))