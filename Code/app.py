from flask import Flask, render_template, redirect, url_for, request
#from histogram import histogram 
from dictogram import Dictogram
from sample import sample_by_frequency 
import os

app = Flask(__name__) 

@app.route('/') 
def index(): 
    #histo = histogram(content)
    histo = Dictogram(content)
    random_word = list()
    for _ in range(10):
        random_word.append(sample_by_frequency(histo)) 
    
    capital = " ".join(random_word).capitalize()
    random_word = f"{capital}."
    return render_template("index.html", random_word=random_word) 

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))