import random
f = open('corpus.txt')
text = f.read().lower().split

class Markov():
    """
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
    
    def __init__(self, text):
        self.chain = {}
        n_words = len(text)
        for _, word_1 in enumerate(text):
            if n_words > _ + 2:
                word_2 = text[_ + 1]
                word = text[_ + 2]
                if (word_1, word_2) not in self.chain:
                    self.chain[(word_1, word_2)] = [word]
                else:
                    self.chain[(word_1, word_2)].append(word)

    def random_walk():
        sentence = random.choice(text)
        while len(sentence) < 10:
            word = random.choice(self.chain(sentence))
            words += '' + word
            sentence.append(words)
        print(sentence)
        
if __name__ == "__main__":
    sentences = Markov.random_walk()
    print(sentences)
