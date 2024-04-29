#live streaming using haar cascade
from flask import Flask, render_template, request, redirect, url_for, Response
import cv2

app = Flask(__name__)

camera=cv2.VideoCapture(0)

def generate_frame():
    while True:
        #read the camera frame
        success, frame= camera.read() #bool variables : success and frame
        if not success:
            # return "Camera is not working"
            break
        else: 
            ret, buffer = cv2.imencode('.jpg', frame) # video ko jpg k frames me buffer me store karwa do!

            #convert this buffer back to bytes. and then return the entire frame
            frame=buffer.tobytes()
         
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n'  + frame + b'\r\n')
        #what are we doing here? we are converting the frame to bytes and then sending it back to the client as a video file!

        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')
    #this funciton will be generatiing video frame and will pass it back to teh index.html



#so what is happeneing here? we are creating a video stream, that is being captured by the camera and then being sent to the client as a video file(frame by frame)


if __name__ == '__main__':
    app.run(debug=True)