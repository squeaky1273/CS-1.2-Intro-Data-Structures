#Thanks for help from Aucoeur
from flask import Flask, render_template, redirect, url_for, request
#from histogram import histogram 
#from dictogram import Dictogram
#from sample import sample_by_frequency
#from markov import markov_chain
from higher_order import higher_markov, random_walk

import os

app = Flask(__name__)

f = open('corpus.txt', 'r') #Open the file for the text
content = f.read().lower().split() #lowercase all of the words
unwanted = dict.fromkeys(map(ord, '\n\r""''.()[],\'!?-;_*:'), None) #remove all punctuation
parse_text = [word.translate(str.maketrans(unwanted)) for word in content] #remove all punctuation from the source text


@app.route('/') 
def index():  
    #histo = histogram(content)
    histo = higher_markov(parse_text) #call higher order markov chain from other file with the edited corpus
    sentence = []
    walk = random_walk(histo)
    for index in range(1):
        sentence.append(walk)
    
    # random_word = ''.join(str(sentence) for sentence in walk)
    for x in range(len(sentence)): #join the words together into sentence instead of separate letters
        random_word = sentence[x]
    
    return render_template("index.html", random_word=random_word) 

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))