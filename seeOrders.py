from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import sqlite3




seeOrders = Blueprint('seeOrders',__name__,static_folder='static',template_folder='templates')



@seeOrders.route('/seeorders')
def showOrdersNames():
    
    #user = request.form['user']
    with sqlite3.connect('Flaskdb.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT OrderInfo,Name FROM Orders')
         #LASKETAAN ORDER ID:T ETTÄ SAADAAN TILAUSTEN MÄÄRÄ SELVILLE.
        cursorMax = connection.cursor()
        cursorMax.execute('SELECT COUNT(OrderId) FROM Orders')
        for order in cursorMax:
            order[0]
        rows = cursor.fetchall()
    return render_template('seeOrders.html',rows = rows,totOrd=order[0])

#checkboxien avulla toteutettu sql-haku ja tulosten näyttö

@seeOrders.route('/selection',methods=['POST','GET'])
def select():

    user = request.form['user']
    #jos orditems checkbox on valittu, toteutetaan alla oleva koodi
    if request.form.get('orditems'):        
        with sqlite3.connect('Flaskdb.db') as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT OrderInfo FROM Orders')
            rows = cursor.fetchall()
            cursorMax = connection.cursor()
            cursorMax.execute('SELECT COUNT(OrderId) FROM Orders')
            for order in cursorMax:
                order[0]
            
            return render_template('seeOrders.html',items=rows,loggedUser=user,totOrd=order[0])
    #orddate checkbox valittu
    elif request.form.get('orddate'):
         with sqlite3.connect('Flaskdb.db') as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT OrderInfo, OrderDate FROM Orders')
            rows = cursor.fetchall()
            cursorMax = connection.cursor()
            cursorMax.execute('SELECT COUNT(OrderId) FROM Orders')
            for order in cursorMax:
                order[0]
            return render_template('seeOrders.html',dates=rows,loggedUser=user,totOrd=order[0])

    elif request.form.get('all'):
      
        with sqlite3.connect('Flaskdb.db') as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Orders')
            rows = cursor.fetchall()
            cursorMax = connection.cursor()
            cursorMax.execute('SELECT COUNT(OrderId) FROM Orders')
            for order in cursorMax:
                order[0]
           
            return render_template('seeOrders.html',rows=rows,loggedUser=user,totOrd=order[0])

@seeOrders.route('/delOrder',methods=['POST','GET'])
def deleteOrder():
    userInput = request.form['userInput']
    if userInput == 'delete':

        with sqlite3.connect('Flaskdb.db') as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('DELETE FROM Orders WHERE OrderId=?',[request.form['orderid']])
            connection.commit()

        return redirect(url_for('seeOrders.showOrdersNames',userInput=userInput))
    elif userInput == 'cancel':
        
        return redirect(url_for('seeOrders.showOrdersNames',userInput=userInput))


      



@seeOrders.route('/logOut',methods=['POST','GET'])
def logOut():
    if request.method == 'POST':
         return render_template('index.html')




