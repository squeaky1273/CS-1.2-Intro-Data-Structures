import random
f = open('corpus.txt')
text = f.read().lower().split
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
def higher_order(text):
    chain = {}
    n_words = (len(text)
    for index, word_1 in enumerate(text):
        if n_words > index + 2:
            word_2 = text[index + 1]
            word_3 = text[index + 2]
            if (word_1, word_2) not in chain:
                chain[(word_1, word_2)] = [text[word_3]]
            else:
                chain[(word_1, word_2)].append(text(word_3))

    return chain

def get_state():
    pass

def random_walk():
    sentence = []
    words = random.choice(text)
    while len(words) < 140:
        word = random.choice(chain(words))
        sentence.append(word)
    print(sentence)
        
if __name__ == "__main__":
    chains = higher_order(text)
    print(chains.chain)
    sentences = chains.random_walk
    print(sentences)
