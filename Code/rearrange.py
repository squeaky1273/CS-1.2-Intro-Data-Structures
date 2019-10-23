import random
from random import choice
import sys

def rearrange(words):
    """Rearrange words that are provided"""
    word_list = []
    random.shuffle(words)
    while words in word_list:
        new_word = choice(words)
        if new_word != word_list:
            word_list.append(new_word)
    return word_list

if __name__ == '__main__':
    words = sys.argv[1:]
    word_list = rearrange(words)
    print(words)
    