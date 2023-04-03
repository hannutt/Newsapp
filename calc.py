from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import re
calc = Blueprint('calc',__name__,static_folder='static',template_folder='templates')

@calc.route('/calc')
def showCalc():
    return render_template('calc.html')


#reititys calculate lomakkeeseen ja laskutoimituksen teko.
@calc.route('/calculate',methods = ['POST','GET'])
def calculate():
    #tallennetaan menu nimisestä valikosta valittu arvo muuttujaan
    value = request.form.get('menu')
    #jos pudotusvalikosta on valittu + eli value muuttujan arvo on + tehdään yhteenlasku
    if request.method == 'POST' and value == '+':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return render_template('calc.html',resultPlace=result)
    elif request.method == "POST" and value == '-':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 - num2
        return render_template('calc.html',resultPlace=result)
    
    elif request.method == "POST" and value == '*':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 * num2
        return render_template('calc.html',resultPlace=result)

    elif request.method == "POST" and value == '/':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 / num2
        return render_template('calc.html',resultPlace=result)