from flask import Flask

app = Flask(__name__)

#defining a decorator(which is basically a rout)
@app.route('/') 
def hello():
    return 'Hello World!'

@app.route('/member') 
def members():
    return 'Hello members!'

@app.route('/gold') 
def gold():
    return 'Hello gold!'

@app.route('/silver') 
def silver():
    return 'Hello silver!'

if __name__=='__main__':
    app.run(debug=True) #used to run restart the server automatically!
