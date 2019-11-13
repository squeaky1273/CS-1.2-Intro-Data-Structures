from dictogram import Dictogram
#from listogram import Listogram
""""
class Markov_chain():
    def __init__(self, words=None):
        self.words = list()
            if words = None:
                pass
"""
f = open('text.txt')
text = f.read().lower().split

# print(text)

def markov_chain(text):
    markov = {}

    for _ in range(len(text)-1):
        word_1 = text[_]
        word_2 = text[_+1]

        #if word_1 in markov.keys():
            #markov[word_1].add_count(word_2)

        #markov[word_1] = Dictogram()
        # print(word_1)
        # print(markov)

        #note: this one works
        if word_1 not in markov.keys():
            markov[word_1] = Dictogram()

        markov.get(word_1).add_count(word_2)

    print(markov)
    return markov

def random_word(markov):
    markov.sample()

def random_walk(markov, word):
    sentence = []
    #sentence.append(word)
    for _ in range(word):
        sentence.append(word)

    return sentence

if __name__ ==  '__main__':
    # random_walk(markov_chain(text))
    markov_chain(text)
