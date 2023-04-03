from flask import Flask,request,url_for,redirect,flash
from flask import render_template,Blueprint
import os

videoPlayer = Blueprint('videoPlayer',__name__,static_folder='static',template_folder='templates')

uploadFolder = 'static/upload'

@videoPlayer.route('/vidplay')
def showPage():
    
    return render_template('videoplayer.html',op='all')

@videoPlayer.route('/size', methods=['POST','GET'])
def sizeChange():
    sizeVal = request.form.get('videoSize')
    #jos select valikosta ei ole valittu mitään eikä change buttonia painettu, soittimen koko on 200x200
    if sizeVal == "":

        return render_template('videoPlayer.html',widthVal=200,heightVal=200)
    elif sizeVal == '300' and request.form.get('changeBtn') == 'change':
         return render_template('videoPlayer.html',widthVal=300,heightVal=300)
    elif sizeVal == '400' and request.form.get('changeBtn') == 'change':
         return render_template('videoPlayer.html',widthVal=400,heightVal=400)


    elif sizeVal == '500' and request.form.get('changeBtn') == 'change':
         return render_template('videoPlayer.html',widthVal=500,heightVal=500)

@videoPlayer.route('/ownLink',methods=['POST','GET'])
def Ownlink():
     #if request.form.get('link'):

     return render_template('videoplayer.html',op='own')

@videoPlayer.route('/upload',methods=['POST','GET'])
def videoUpload():
      return render_template('videoplayer.html',op='video')

@videoPlayer.route('/uploader',methods=['POST','GET'])
def uploader():
     #f-muuttujaan tallennetaan file nimisen-html lomakkeen kautta saaatava tiedosto
     f = request.files['file']
     #yhdistetään uploadfolder eli polku ja sinne tallennettava tiedosto ja sen nimi
     f.save(os.path.join(uploadFolder,f.filename))
     return 'Video uploaded'
'''
@videoPlayer.route('/play',methods=['POST','GET'])
def open():
    filepath = request.form['filepath']
    return render_template('videoPlayer.html',videoPlace=filepath)
    '''



