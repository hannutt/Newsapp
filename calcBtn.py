from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint

calcBtn = Blueprint('calcBtn',__name__,static_folder='static',template_folder='templates')

@calcBtn.route('/calcBtn')
def showPage():

    return render_template('calcWithBtn.html')

@calcBtn.route('/calculateBtn',methods=['POST','GET'])
def executeCal():
    
    
    #num3 ja #num4 ovat calculateBtn formin sisällä olevia piilotettuja input kenttiä
    #joihin calculate javascript funktio asettaa samat numerot kuin näkyviin input kenttiin
    total = 0
    number1 = int(request.form['num3'])
    op = request.form['operator']
    number2 = int(request.form['num4'])
    
    if op == '+':
        total = number1 + number2
       
    elif op == '*':
        total = number1 * number2
   
    elif op == '-':
        total = number1 - number2
    elif op == '/':
        total = number1 / number2

    elif op == 'pow':
        total = pow(number1,number2)
    return render_template('CalcWithBtn.html',row1=number1,row2=op,row3=number2,res=total)