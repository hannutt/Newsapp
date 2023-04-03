from flask import Flask, request, url_for, redirect, flash,session
from flask import render_template, Blueprint
import random

wdclone = Blueprint('wdclone', __name__,static_folder='static', template_folder='templates')

@wdclone.route('/startwd')
def startWd():

    global words
    words = ['Good','bad','coffee','charger','car','bike']
    global answers
    answers = ['hyvä','huono','kahvi','laturi','auto','pyörä']
    global randowWord
    randowWord = random.choice(words)
    #words ja answer listan indeksi paikat vastaavat toisiaan eli words[0] == answers[0]
    #selvitetään random wordin indeksiluku eli paikka words-listassa
    wordsIndex = words.index(randowWord)
    global answerIndex
    #answerindexiin sijoitetaan answers listan arvo joka vastaa words listan indeksiarvoa
    answerIndex = answers[wordsIndex]

    #result muuttujan välitys checkword funktiosta startwd funktioon.
    result= request.args.get('result')
    
    check = request.args.get('check')
    return render_template('wdclone.html',wordPlace=randowWord,resultPlace=result,checkPlace=check)

@wdclone.route('/checkWord',methods=['POST','GET'])
def checkWords():
    word = request.form['word']
    word = word.lower()
    #jos kirjoitettu sana on sama kuin indeksipaikassa oleva sana
    if word == answerIndex:
        
        #redirectin avulla saadaan oikean vastauksen jälkeen renderöityä correct teksti
        #ja uusi satunnaissana listalta automaattisesti eli kutsutaan html-sivua ja startWd funktiota.
        return redirect(url_for('wdclone.startWd',result='correct',check='OK'))
    #jos kirjoitetun sanan ja kysytyn sanan ensimmäinen kirjain on sama
    elif word[0] == answerIndex[0]:
        return redirect(url_for('wdclone.startWd',result='first letter was right!',check=''))
    #jos vastaus on väärä renderöidään pelkästään wdclone.html uudelleen
    else:
        return render_template('wdclone.html',wordPlace=randowWord,answerPlace='Wrong, try again!')
  
   
    
