from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Load Haar cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

camera = cv2.VideoCapture(0)

def generate_frame():
    while True:
        # Read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # Convert the frame to grayscale for face and eye detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            # Draw rectangles around the faces and eyes
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)

            # Convert the buffer to bytes
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
