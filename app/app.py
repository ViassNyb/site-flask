from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/siri')
def siri():
    return render_template('siri.html')

@app.route('/google_assistant')
def google_assistant():
    return render_template('google_assistant.html')

@app.route('/alexa')
def alexa():
    return render_template('alexa.html')

@app.route('/cortana')
def cortana():
    return render_template('cortana.html')

@app.route('/alisa')
def alisa():
    return render_template('alisa.html')

if __name__ == '__main__':
    app.run(debug=True)
