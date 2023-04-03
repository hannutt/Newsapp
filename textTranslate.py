from flask import Flask, request, url_for, redirect, flash
from flask import render_template, Blueprint
from translate import Translator

textTranslate = Blueprint('textTranslate', __name__,static_folder='static', template_folder='templates')

@textTranslate.route('/startTranslate')

def startTranslate():

    return render_template('textTranslate.html')

@textTranslate.route('/doTranslate',methods=['POST','GET'])
def doTrans():
    word = request.form['translateWord']
    fromLn = request.form.get('fromLang')
    toLn = request.form.get('toLang')
    translator= Translator(from_lang=fromLn,to_lang=toLn)
    translation = translator.translate(word)

    return render_template('textTranslate.html',wordPlace=translation)