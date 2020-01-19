import os
from flask import Flask, request, render_template, url_for, redirect, send_file
import word_to_img


app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('index.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.save(os.path.join('/Users/nithilanpugal/PycharmProjects/Speachto/venv/YTSLI-master-2', photo.filename))
            v2w = word_to_img.voice_to_words(os.path.join('/Users/nithilanpugal/PycharmProjects/Speachto/venv/YTSLI-master-2', photo.filename))
            caption = word_to_img.captions(v2w)
            caption.save('test123.jpg')
    return redirect(url_for('fileFrontPage'))



@app.route("/test123.jpg", methods = ['GET'])
def handleDownload():
    return send_file('test123.jpg')


if __name__ == '__main__':
    app.run()
