from flask import Flask, request, url_for, redirect, flash
from flask import render_template, Blueprint
import sqlite3

register= Blueprint('register',__name__,static_folder='static',template_folder='templates')

@register.route('/register')
def showPage():

    return render_template('register.html')

@register.route('/regUser',methods=['POST','GET'])
def registerUser():
    username = request.form['username']
    password = request.form['password']
    passwordagain = request.form['passwordagain']
    connection = sqlite3.connect('Flaskdb.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT username FROM LOGIN WHERE username=?',(username,))
    row = cursor.fetchone()
    if row or password != passwordagain:
        return render_template('unsuccess.html',ad='the username is already in use or the password confirmation went wrong')
    else:
        cursor.execute('INSERT INTO LOGIN (username,password) VALUES (?,?)',(username,password,))
        connection.commit()
        return render_template('success.html',adPlace='Register OK!')
