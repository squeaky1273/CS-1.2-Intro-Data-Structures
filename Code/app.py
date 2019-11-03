from flask import Flask, render_template 
from histogram import histogram 
from sample import sample_by_frequency 
import os 

app = Flask(__name__) 

@app.route('/') 
def index(): 
    f = open('text.txt', 'r')
    word = f.read()
    hist = histogram(10)
    random = sample_by_frequency(histogram)
    return render_template("index.html", word=random) 

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))