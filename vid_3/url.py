from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return "In this video we will be learning about the routes and dynamic URL building through Python's Flask framework"

@app.route('/success/<int:score>')
def success(score):
    return "Congratulations on passing the subject. You scored " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Alas! you will have to do it all over again. Coz your score is " + str(score)

@app.route('/results/<int:marks>')
def result(marks):
    if marks > 90:
        return redirect(url_for('success', score=marks))
    else:
        return redirect(url_for('fail', score=marks))

if __name__ == '__main__':
    app.run(debug=True)
