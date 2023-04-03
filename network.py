import json
from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import socket
import speedtest
import plotly
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


network = Blueprint('network',__name__,static_folder='static',template_folder='templates')

@network.route('/networkInfo')
def showIP():
    hostname = socket.gethostname()
    IpAdd = socket.gethostbyname(hostname)
 
    return render_template('network.html',ipPlace=IpAdd,hostPlace=hostname)

@network.route('/connectiontest',methods=['POST','GET'])
def calcSpeed():
    byte = 1048576
    speed_test = speedtest.Speedtest()
    download_speed = speed_test.download()
    upload_speed = speed_test.upload()
    #jaetaan tulos byte muuttujan arvolla
    divideDownload = download_speed / byte
    divideUpload = upload_speed / byte
    #pyöristetään tulos 1 desimaalin tarkkuuteen
    global finalSpeedInt
    global finalUploadInt
    finalSpeedInt = round(divideDownload,1)
    finalUploadInt = round(divideUpload,1)
    #muunto merkkijonoiksi, että render templaten parametreiisa voidaan yhdistää muuttuja 
    # ja merkkijono Mb/s.
    finalSpeed = str(finalSpeedInt)
    finalUpload = str(finalUploadInt)
    #barChart()
 
    return render_template('network.html',downloadPlace=finalSpeed+' MB/s',uploadPlace=finalUpload+' MB/s')


#cauge kaavion piirto arvona mitattu latausnopeus
#@network.route('/showChart',methods=['POST','GET'])
def caugeChart():
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = finalSpeedInt,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Download and upload speed"}))
    fig.show()
    #return render_template(fig.show())

def barChart():
    speeds=['Download', 'Upload']

    fig = go.Figure([go.Bar(x=speeds, y=[finalSpeedInt,finalUploadInt])])
    fig.show()
      
      

    