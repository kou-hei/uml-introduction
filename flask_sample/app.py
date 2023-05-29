from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/') 
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/next')
def next():
    return 'next page'

@app.route('/sample')
def sample():
    return render_template('index.html')