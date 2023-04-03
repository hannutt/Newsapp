#import matplotlib.pyplot as plt
from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import plotly
import plotly.express as px
import plotly.graph_objects as go
from matplotlib.figure import Figure
from tkinter import filedialog
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
import numpy as np


import base64
from io import BytesIO


charts = Blueprint('charts',__name__,static_folder='charts',template_folder='templates')

#etusivu
@charts.route('/chartspage')
def openPage():
    return render_template('charts.html')

@charts.route('/chartsBar',methods=['POST','GET'])
def ChartsBar():
        #lähetetään charts.html sivulle tieto, että op on bar
        
        return render_template('charts.html',op='bar')

@charts.route('/chartsPie',methods=['POST','GET'])
def ChartsPie():
        #lähetetään charts.html sivulle tieto, että op on bar
        
        return render_template('charts.html',op='pie')

@charts.route('/Bar',methods=['POST','GET'])
def Bar():
         
         return render_template('charts.html')
        
        


#kaavioiden piirto, 
@charts.route('/drawPlots',methods=['POST','GET'])
def drawPlot():
    
    value = request.form.get('size')
    colorvalue = request.form.get('color')
    if request.form.get('DrawBtn') == 'drawChart':
         val1 = request.form['startVal']
         val2 = request.form['endVal']
     # Generate the figure **without using pyplot**.
     #facecolor on taustaväri, colorvalue muuttujaan on tallennettu
     #color dropdownista valittu väri.
         global fig
         fig = Figure(facecolor=colorvalue)
         ax = fig.subplots()
         #käyttäjän syöttämät arvot parametreina
         ax.plot([val1,val2])
    # Save it to a temporary buffer.
         buf = BytesIO()
         fig.savefig(buf, format="png")

                
    # Embed the result in the html output.
         data = base64.b64encode(buf.getbuffer()).decode("ascii")
         if value == '500':
            #plot_url on charts.html sivulla oleva img src tagin muuttujapaikka
            #chartWidth ja chartHeight ovat chart.html sivulla olevia width ja height tageihin sijoitettuja
            #muuttujia.
            return render_template('charts.html',plot_url=data,chartWidth = 500,chartHeight = 500)
         elif value == '600':
            return render_template('charts.html',plot_url=data,chartWidth = 600,chartHeight = 600)
         elif value == '700':
            return render_template('charts.html',plot_url=data,chartWidth = 700,chartHeight = 700)
         elif value == '800':
            return render_template('charts.html',plot_url=data,chartWidth = 800,chartHeight = 800)
            

@charts.route('/saveDraw',methods=['POST','GET'])
def saveFig():
     if request.form.get('saveBtn') == 'saveChart': 
        
        #tiedostopääte, jolloin sitä ei tarvitse erikseen lisätä tiedoston nimen perään
        extension = [('PNG-file', '*.png')]
        #tallennettavan tiedoston nimi
        file = filedialog.asksaveasfilename(filetypes=extension,defaultextension=extension)
        #tiedoston nimi parametrina, formaattina .png
        fig.savefig(file,format='png')
        

        return render_template('charts.html')












 

