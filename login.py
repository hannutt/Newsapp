from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import sqlite3

login = Blueprint('login',__name__,static_folder='static',template_folder='templates')

@login.route('/loginpage')
def showLogPage():
    return render_template('login.html')


@login.route('/loginForm',methods=['POST','GET'])
def loginToPage():
    

    if request.method == 'POST':
       
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('Flaskdb.db') as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.execute('SELECT * FROM LOGIN WHERE USERNAME=? AND PASSWORD=?',(username,password))
            
            row = cursor.fetchone()
            if row:
                #cursorMax = connection.execute('SELECT MAX(OrderId) FROM orders')
                cursor.execute('SELECT * FROM Orders')
                rows = cursor.fetchall()
                cursorMax = connection.cursor()
            #LASKETAAN ORDER ID:T ETTÄ SAADAAN TILAUSTEN MÄÄRÄ SELVILLE.
                cursorMax.execute('SELECT COUNT(OrderId) FROM Orders')
                for order in cursorMax:
                    order[0]
                #rows2 = cursorMax.fetchone()
                #usr = request.form['loguser']
                return render_template('seeOrders.html',rows=rows,loggedUser=username,totOrd=order[0])
            
            else:
                
                #return redirect(url_for('login.loginToPage'), 404)

                return render_template('unsuccess.html',ad='Log in to see this page!')

