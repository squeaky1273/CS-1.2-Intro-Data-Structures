from flask import Flask, render_template, redirect, url_for, request
#from histogram import histogram 
#from dictogram import Dictogram
#from sample import sample_by_frequency
#from markov import markov_chain
from higher_order import higher_markov, random_walk

import os

app = Flask(__name__)

f = open('corpus.txt', 'r')
content = f.read().lower().split()
unwanted = dict.fromkeys(map(ord, '\n\r""''.()[],\'!?-;_*:'), None)
parse_text = [word.translate(str.maketrans(unwanted)) for word in content]


@app.route('/') 
def index():  
    #histo = histogram(content)
    histo = higher_markov(parse_text)
    random_word = []
    for index in range(10):
        random_word.append(random_walk(histo))
    
    return render_template("index.html", random_word=random_word) 

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))