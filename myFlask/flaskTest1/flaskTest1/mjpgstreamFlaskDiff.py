from flask import Flask,Response
import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

def getGrayCameraImage(f):
    gray_img = cv2.cvtColor(f, cv2.COLOR_RGB2GRAY)
    return gray_img

app = Flask(__name__)
def generate():

    ret, img = cam.read()
    old_img = getGrayCameraImage(img)
    
    while True:
        ret,img = cam.read()
        cur_img = getGrayCameraImage(img)
        diff_img = cv2.absdiff(old_img,cur_img)
        jpegdata=cv2.imencode(".jpeg",diff_img)[1].tostring()
        old_img = cur_img.copy()
        string = "--MjpgBound\r\n"
        string += "Content-Type: image/jpeg\r\n"
        string += "Content-length: "+str(len(jpegdata))+"\r\n\r\n"
        yield (string.encode("utf-8") + jpegdata + "\r\n\r\n".encode("utf-8"))

@app.route('/stream')
def do_stream():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=--MjpgBound')

@app.route('/')
def do_route():
    return "<HTML><BODY><img src=\"stream\" width=320 height=240></BODY></HTML>"

if __name__ == "__main__":
    app.run(host='localhost', port=8008)
