from flask import Flask, request, url_for, redirect, flash
from flask import render_template, Blueprint
import sqlite3
import time
import datetime
from datetime import date
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


webshop = Blueprint('webshop', __name__,static_folder='static', template_folder='templates')
global showWebShop
global colorMark
colorMark = '||'


@webshop.route('/Webshop')
def showWebShop():

    connection = sqlite3.connect('Flaskdb.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT idnum,Price,img,descr,instock FROM SHOP')
    rows = cursor.fetchall()
    cursorProd = connection.cursor()
    cursorProd.execute('SELECT COUNT(Idnum) FROM Shop')
    for prod in cursorProd:
        prod[0]
    return render_template('Webshop.html', rows=rows, stockPlace=colorMark, totProd=prod[0])


@webshop.route('/sendDiscCode', methods=['POST', 'GET'])
def discPrices():
    discount = request.form['discount']
    with sqlite3.connect('Flaskdb.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.execute(
            'SELECT * FROM discount WHERE discountCode=?', (discount,))
        row = cursor.fetchone()
        if row:
            cursor.execute(
                'SELECT idnum,DiscPrice AS Price,img,descr,instock FROM SHOP')
            rows = cursor.fetchall()
            return render_template('Webshop.html', rows=rows, stockPlace=colorMark)
        else:
            return render_template('Unsuccess.html', ad='Wrong discount code!')

# NÄYTETÄÄN TUOTTEET HALVIMMASTA ALKAEN


@webshop.route('/cheapest', methods=['POST', 'GET'])
def CheapestProd():

    connection = sqlite3.connect('Flaskdb.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SHOP ORDER BY Price ASC')
    rows = cursor.fetchall()

    return render_template('Webshop.html', rows=rows, stockPlace=colorMark)

# kallein tuote ensin


@webshop.route('/expensive', methods=['POST', 'GET'])
def expensiveProd():

    connection = sqlite3.connect('Flaskdb.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SHOP ORDER BY Price DESC')
    rows = cursor.fetchall()

    return render_template('Webshop.html', rows=rows, stockPlace=colorMark)


global cart
cart = []
global pricelist
pricelist = []
global quantity
quantity = []
global prodlist
prodlist = []


@webshop.route('/AddCart', methods=['POST', 'GET'])
def orders():

    connection = sqlite3.connect('Flaskdb.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT idnum,price,img,descr,instock,pcode FROM SHOP')
    rows = cursor.fetchall()
    if request.method == 'POST':

        # amount ja price int-muunoksena että voidaan laskea yht.hinta total muuttujaan
        # tietokannan tietojen tallennus piilotetuista input kentistä muuttujiin
        # pcode = request.form['pcode']
        global quantitySum
        amount = int(request.form['amount'])
        quantity.append(amount)
        quantitySum = sum(quantity)

         # kappalemäärän tarkistus, jos se on nolla näytetään unsuccess.html jos enemmän lisätään se koriin
        if amount == 0:
            # redirect eli näytetään virheilmoitus ja linkki takaisin webshop sivulle
            return redirect(url_for('webshop.showWebShop'), 404)
            # return render_template('Unsuccess.html',ad='Set amount!')

        else:
            prod = request.form['prod']
            price = int(request.form['price'])
            total = price * amount
            # olista hinnoille, että ne voidaan lopuksi laskea yhteen sum-metodilla
            pricelist.append(total)
            # globaali muuttuja, että sitä voidaan sendorders funktiossa
            global OrderSum
            # pricelist listan alkioiden yhteenlasku
            OrderSum = sum(pricelist)
            Order = (amount, prod, total)

            cart.append(Order)
            #flash(prod + ' added to cart!')
            return render_template('Webshop.html', rows=rows, stockPlace=colorMark)


@webshop.route('/sendOrd', methods=['POST', 'GET'])
def SendOrders():
    # jos lista on tyhjä eli koriin ei ole lisätty tuotteita näytetään unsuccess.html ja ilmoitus
    # tyhjästä korista.
    if len(cart) == 0:
        return render_template('unsuccess.html', ad='Your cart is empty!')
    else:
        currentdate = datetime.datetime.now()
        formatDate = currentdate.strftime('%d.%m.%y.%H:%M')

        return render_template('sendOrder.html', listPlace=cart, orderTime=formatDate, sumPlace=OrderSum, quantityPlace=quantitySum)


@webshop.route('/SaveDetails', methods=['POST', 'GET'])
def saveDetails():
    orderDate = request.form['orderDate']
    name = request.form['flname']
    address = request.form['addr']
    phone = request.form['phone']
    email = request.form['email']

    if request.method == 'POST':
        with sqlite3.connect('Flaskdb.db') as connection:
            cursor = connection.cursor()

        
            #tallennetaan muuttujaan cart-listan sisältö joka muutetaan ensin merkkijonoksi.
            #sqlite ei muuten tallenna sitä.
            cartStr = str(cart)

                
            
               

                # email-osoitteen tark. jos @ ja .puuttuu näytetään siitä ilmoitus
            if email.find('@') == -1 and email.find('.') == -1:

                return render_template('SendOrder.html', emailWrong='Email address is not correct')

            elif email.find('@') == -1 or email.find('.') == -1:
                return render_template('SendOrder.html', emailWrong='Email address is not correct')

            
            else:

                cursor.execute('INSERT INTO Orders (OrderInfo,Name,Address,Phone,Email,OrderDate,Quantity,OrderPrice)   VALUES (?,?,?,?,?,?,?,?)', (cartStr, name, address, phone, email, orderDate, quantitySum, OrderSum))
                connection.commit()
                #sendEmail()
                return render_template('success.html',adPlace='Order sent!')
# sähköpostin lähetys tilauksesta
def sendEmail():
     subject = "New Order!"
     body = "You have a new order!"
     sender_email = "workapptest@yahoo.com"
     receiver_email = "htuomela@gmail.com"
     password = "birnclvcfpfqscng"

     message = MIMEMultipart()
     message["From"] = sender_email
     message["To"] = receiver_email
     message["Subject"] = subject

     message.attach(MIMEText(body, "plain"))
     text = message.as_string()
     
     context = ssl.create_default_context()

     with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465, context=context) as server:

        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email,text)
                    

                    

                    


    
# tuotteen poisto listalta
@webshop.route('/delFromList',methods=['POST','GET'])
def delFromList():
    # delValue = int(request.form.get('Delmenu'))
    
    # delete = request.form['delprod']
    cart.pop(0)
    pricelist.pop(0)

    return render_template('sendOrder.html',listPlace=cart)

@webshop.route('/searchproduct',methods=['POST','GET'])
def searchProd():
    srcvalue = request.form['searchprod']
    with sqlite3.connect('Flaskdb.db') as connection:

            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            #sql haku tuotenimellä, näytetään tuotenimi,hinta ja varastotilanne. srcvalue parametrin eteen
            # ja taakse % merkit että LIKE hakuehto toimii eli voi hakea kirjoittamalla vain osan tuotenimestä
            cursor.execute('SELECT DESCR,PRICE,INSTOCK FROM SHOP WHERE DESCR=? OR DESCR LIKE ?',(srcvalue,'%'+srcvalue+'%'))
            searchrows = cursor.fetchall()
            if len(searchrows) == 0:
                return render_template('webshop.html',rows=searchrows,NotFound='Product is not available')
            else:
                return render_template('webshop.html',rows=searchrows)

