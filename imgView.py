from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import os
from werkzeug.utils import secure_filename
import urllib.request
from fileinput import filename




imgView = Blueprint('imgView',__name__,static_folder='static',template_folder='templates')

uploadFolder = 'static/upload'


@imgView.route('/uploadimg')
def uploadPage():
    return render_template('imgView.html')

#html lomakkeen kautta valitun kuvan tallennus
@imgView.route('/uploader',methods=['POST','GET'])
def uploadImg():
    #f-muuttujaan tallennetaan file nimisen-html lomakkeen kautta saaatava tiedosto
    f = request.files['file']
    #yhdistetään uploadfolder eli polku ja sinne tallennettava tiedosto ja sen nimi
    f.save(os.path.join(uploadFolder,f.filename))
      
 
    return 'Image uploaded'



@imgView.route('/displayer',methods=['POST','GET'])
def open():
    filepath = request.form['filepath']
    return render_template('imgView.html',imgPlace=filepath)