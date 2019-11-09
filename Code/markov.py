from dictogram import Dictogram
#from listogram import Listogram
""""
class Markov_chain():
    def __init__(self, words=None):
        self.words = list()
            if words = None:
                pass
"""
f = open(text.txt)
text = f.split

def markov_chain(text):
    for _ in range(len(text)-1):
     (text[_], text[_+1])

    pairs = markov_chain(text)

    markov = {}
    for word_1, word_2 in pairs:
        if word_1[_] in markov.keys:
            markov[word_1.append(word_2)
        else:
            markov[word_1] = [word_2]
        return markov

def random_word():
    pass

def random_walk(word):
    sentence = []
    sentence.append(word)
    for _ in range(word):
        sentence.append(word)
    
    return sentence
    pass

if __name__ ==  '__main__':
    random_walk(markov_chain(text))