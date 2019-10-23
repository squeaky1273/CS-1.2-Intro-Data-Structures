from random import choice
import sys

def sentence(number):
    """Create sentences with the provided words"""
    f = open('/usr/share/dict/words', 'r')
    word_list = f.read().splitlines()
    f.close()
    sentence = []
    count = 0
    while count < int(number):
        words = choice(word_list)
        sentence.append(words)
        count += 1
    return (" ".join(sentence))

if __name__ == "__main__":
    number = sys.argv[1]
    print(sentence(number))