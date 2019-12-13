from dictogram import Dictogram
from Queue import Queue
from random import choice

f = open('corpus.txt')
text = f.read().lower().split()

def higher_markov(text):
    chain = {}
    for index in range(len(text)-2):
        word_1 = text[index]
        word_2 = text[index + 1]
        word_3 = text[index + 2]
        key = (word_1, word_2)
        if key not in chain.keys():
            chain[key] = Dictogram()
        
        chain.get(key).add_count(word_3)

    return chain
    print(chain)

def random_words(chain):
    all_tuples = chain.keys()
    random_tuple = choice(list(all_tuples))
    markov = chain.get(random_tuple)
    return markov.sample()

def random_walk(chain):
    sentence = []
    index = 0
    for word in range(10):
        states = random_words(chain) # this gets first random word

        rand_state = choice(states)

        next_word = rand_state[index]

        next_word = random_words(chain)

        sentence.append(next_word)

    #for word in range(10):
        
        #states = random_word(chain) # this gets first random word
        
        #next_word = [states[1], word]

        #for next_word in range(10):
            #sentence.append(next_word)

    return sentence
        
if __name__ == "__main__":
    f = open('corpus.txt')
    text = f.read().lower().split()
    """
    markov = higher_order(text)
    print(markov.chain)
    sentences = markov.random_walk()
    print(sentences)
    """
    markov = higher_markov(text)
    random_word = random_words(markov)
    sentence = random_walk(random_word)
    print(sentence)
    #print(random_walk(higher_markov(text)))
