from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import sqlite3


AddProduct = Blueprint('AddProduct',__name__,static_folder='static',template_folder='templates')

@AddProduct.route('/AddProduct')
def AddPage():


    return render_template('AddProduct.html')

@AddProduct.route('/Add',methods=['POST','GET'])
def AddNew():

    name = request.form['productname']
    price = request.form['productprice']
    instock = request.form['productstock']
    connection = sqlite3.connect('Flaskdb.db')
    
    cursor = connection.cursor()
    cursor.execute('INSERT INTO SHOP (DESCR,PRICE,INSTOCK) VALUES (?,?,?)', (name,price,instock))
    connection.commit()
    return render_template('success.html',adPlace='Product Added!')
