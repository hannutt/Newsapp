from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint


chatbot = Blueprint('chatbot',__name__,static_folder='static',template_folder='templates')

@chatbot.route('/chatbot')
def showPage():

    return render_template('chatbot.html')

@chatbot.route('/symptonsForm',methods=['POST','GET'])
def readSymptons():
    Emergencyvalue = request.form.get('chatmenu')
    Infovalue = request.form.get('chatmenu')
    #dictionaryn avulla valitaan hätänumero eli oikea avain arvo pari
    #eli chatbot.html selection menun valuea vastaava arvo
    
    emergencyNumbDict = {
        '112':'112',
        '911':'911',
        '999':'999',
        '100':'100'
    }

    healtCareInfo = {
        '112':'116117',
        '100':'111'
    }

 
    #dictionarysta haettu arvo tallennetaan value muuttujaan
    Emergencyvalue = emergencyNumbDict.get(Emergencyvalue)
    Infovalue = healtCareInfo.get(Infovalue)
    
    symptonsList = ['help','tired','headache','pain','anxiety']
    seriousList = ['suicidal','suicide','depression']
    if request.method == 'POST':
        symptons = request.form['sympton']
        symptons = symptons.lower()

        result = any(Symptons in symptons for Symptons in symptonsList)
        result2 = any(Symptons in symptons for Symptons in seriousList)
        if result2 == True:
            return render_template('chatbot.html',answerPlace='Call to emergency number '+Emergencyvalue)
        elif result == True:
            return render_template('chatbot.html',answerPlace=' Get a painkiller and try to get some sleep. you can also call: '+Infovalue)

        elif result == False:
            return render_template('chatbot.html',answerPlace='You seem to be OK')