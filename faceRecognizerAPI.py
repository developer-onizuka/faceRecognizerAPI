#!/usr/bin/python3
import cv2
import subprocess
import base64
import face_recognition
from flask import Flask, request, render_template, Response

app = Flask(__name__)

def run_command(command):
    #return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    return subprocess.check_output(command).decode('utf-8')

def encBase64(inputfile):
    with open(inputfile, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def decBase64(bs, outputfile):
    with open(outputfile, "wb") as f:
        f.write(base64.b64decode(bs))

#####

@app.route('/<command>')
def command_server(command):
    return run_command(command)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/text", methods=['GET','POST'])
def file_server():
    try:
        if request.method == 'GET':
            return request.args.get('value', '')
        elif request.method == 'POST':
            #return request.form['query']
            return render_template("index.html", value=request.form['value']) 
        else:
            return abort(400)
    except Exception as e:
        return str(e)

@app.route("/facerecognizer", methods=['GET','POST'])
def uploads_file():
    try:
        inputFile = "/tmp/input.jpg"
        if request.method == 'POST':
            fs = request.files['img']
            fs.save(inputFile)
            #return render_template("index.html", value=fs) 

            im = cv2.imread(inputFile)
            imRGB = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
            facePositions = face_recognition.face_locations(imRGB,model='cnn')
            return render_template("json.html", value=facePositions)
            #return render_template("index.html", value=facePositions)

            #binaryData = encBase64(inputFile)
            #decBase64(binaryData, outputFile)
            #imgsrc = "data:image/jpeg;base64,"+ binaryData
            #return render_template('index.html', img_path=imgsrc)

    except Exception as e:
        return str(e)

#####

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
