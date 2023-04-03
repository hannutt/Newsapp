from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint


quiz = Blueprint('quiz',__name__,static_folder='static',template_folder='templates')


@quiz.route('/quiz')
def Questions():
    #globaali muuttuja, että sitä voidaan käyttää startquiz funktiossa
    global questions
    #lista for looppaus quiz.html:ssä.
    questions = ['Is Berlin capital of Germany?','Is Paris capital of France?', 'Is Moscow capital of Russia','Is Helsinki capital Of Finland']
   
    return render_template('quiz.html',questPlace=questions[0],questPlace2=questions[1],questPlace3=questions[2],questPlace4=questions[3])

@quiz.route('/quizForm', methods=['POST','GET'])
def startQuiz():
    value = request.form['q1']
    value2 = request.form['q2']
    value3 = request.form['q3']
    value4 = request.form['q4']
    answers=(value,value2,value3,value4)
    points = 0
    #tallennetaan listan alkioiden määrä total muuttujaan jolloin saadaan maksipisteet selville
    total = len(questions)

    #jos answers tuplessa on true ja false-arvot, lasketaan true arvojen määrä
    # ja sen perusteella pisteet.
    
    if 'True' and 'False' in answers:
        count = answers.count('True')
        points = points + count
        return render_template('quiz.html',answerPlace='Something went wrong!',pointsPlace=points,totalPlace=total,var='done')
    elif 'True' in answers:
        count = answers.count('True')
        points = points + count
        return render_template('quiz.html',answerPlace='Good!',pointsPlace=points,totalPlace=total,var='done')

@quiz.route('/tryAgain',methods=['POST','GET'])
def tryAgain():

    return redirect(url_for('quiz.Questions'))
