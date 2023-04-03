from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import sqlite3

ChangePsw = Blueprint('ChangePsw',__name__,static_folder='static',template_folder='templates')

@ChangePsw.route('/changePage')
def showChangePage():
    return render_template('changepsw.html')

@ChangePsw.route('/changePsw',methods=['POST','GET'])
def change():
    username = request.form['username']
    currentpsw = request.form['currentpsw']
    newpsw = request.form['newpsw']
    newagain = request.form['newagain']
    connection = sqlite3.connect('Flaskdb.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT username, password FROM LOGIN WHERE username=? AND password=?',(username,currentpsw,))
    row = cursor.fetchone()
    #jos row on True eli syötettyä salasanaa vastaava salana löytyy kannasta
    if row and newpsw == newagain:
        cursor.execute('UPDATE LOGIN SET password=? WHERE username=?',(newpsw,username,))
        connection.commit()
        return render_template('success.html',adPlace='Password is changed!')
    else:
        return render_template('unsuccess.html',ad='Something went wrong!')