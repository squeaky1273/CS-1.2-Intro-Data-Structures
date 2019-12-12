
f = open('corpus.txt')
text = f.read().lower().split()
from dictogram import Dictogram

"""
class Queue():
    def __init__():
        self.queue = list()
    
    def __str__(self):
        return self.queue.__str__()

    def enqueue(self):
        self.queue.append(item)

    def dequeue(self):
        if not len(self.queue) == 0:
            item = self.queue.delete(0)
            return item
        else:
            raise IndexError('No items in queue.')

    def iterate(self):
        if not len(self.queue) == 0:
            for item in self.queue:
                yield(item)
        else:
            raise IndexError('No items in queue.')
"""
def higher_markov(text):
    chain = {}
    for index in range (len(text)-1):
        word_1 = text[index]
        word_2 = text[index + 1]
        word_3 = text[index + 2]
        key = (word_1, word_2)
        if key not in chain.keys:
            chain[key] = Dictogram()
    
        chain.get[key].append(text(word_3))

    return chain

def random_word(chain):
    chain.sample()

def random_walk():
    sentence = []
    for word in words:
        sentence.append(word)
    return sentence
        
if __name__ == "__main__":
    """
    markov = higher_order(text)
    print(markov.chain)
    sentences = markov.random_walk()
    print(sentences)
    """
    random_walk(higher_markov(text))
