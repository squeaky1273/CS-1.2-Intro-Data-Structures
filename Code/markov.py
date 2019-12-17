from dictogram import Dictogram
#from listogram import Listogram
""""
class Markov_chain():
    def __init__(self, words=None):
        self.words = list()
            if words = None:
                pass
"""
f = open('corpus.txt')
text = f.read().lower().split

# print(text)

def markov_chain(text):#Create a chain to scramble the words based on frequency and Dictogram
    markov = {}

    for index in range(len(text)-1):
        word_1 = text[index]
        word_2 = text[index+1]

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

def random_word(markov):#Choose a random word from the markov chain
    return markov.sample()

def random_walk(word):#Create a sentence based on the random words from the markov chain
    sentence = []
    for word in text:
        sentence.append(random_word)
    print(sentence)

if __name__ ==  '__main__':
    random_walk(markov_chain(text))
    #markov_chain(text)
    
