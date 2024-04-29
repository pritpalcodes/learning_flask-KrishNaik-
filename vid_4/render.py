from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def say_hi():
    return render_template('index.html')

@app.route('/success/<int:score>')  
def success(score):
    return render_template('success.html', score=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('fail.html', score=score)

@app.route('/results/<int:marks>')
def result(marks):
    if marks > 40:
        return redirect(url_for('success', score=marks))
    else:
        return redirect(url_for('fail', score=marks))



if __name__ == '__main__':
    app.run(debug=True)
