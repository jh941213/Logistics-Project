from flask import Flask, render_template, Response
from camera import VideoCamera
from ocr import OCRDetect
import os
import shutil

app = Flask(__name__)

switch = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect')
def detect():
    global switch
    switch = 1
    return render_template('camera.html')

@app.route('/ocr')
def ocr():
    global switch
    switch = 2
    return render_template('ocr_detect.html')

count = 0

def gen_det(camera):
    while True:
        if count % 3 == 0:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n\r\n')



@app.route('/video_feed', methods=['GET'])
def video_feed():
    if os.path.exists("./runs/detect"):
            shutil.rmtree("./runs/detect")
    global switch
    if switch == 1:
        return Response(gen_det(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    elif switch == 2:
        return Response(gen_det(OCRDetect()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)