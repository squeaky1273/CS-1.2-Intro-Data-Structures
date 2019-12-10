from flask import Flask, render_template, redirect, url_for, request
#from histogram import histogram 
#from dictogram import Dictogram
from sample import sample_by_frequency
from markov import markov_chain, random_walk

import os

app = Flask(__name__)

f = open('corpus.txt', 'r')
content = f.read().split()

@app.route('/') 
def index():  
    #histo = histogram(content)
    histo = markov_chain(content)
    random_word = list()
    for _ in range(10):
        random_word.append(sample_by_frequency(histo)) 
    
    return render_template("index.html", random_word=random_word) 

    low = ''.join(content).lower()
    print(low)

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))