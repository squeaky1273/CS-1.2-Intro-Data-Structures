from random import choice
import sys

def rearrange(words):
    """Rearrange words that are provided"""
    word_list = []
    count = 0
    while count < len(words):
        new_word = choice(words)
        if new_word not in word_list:
            word_list.append(new_word)
            count += 1
    return (" ".join(word_list))

if __name__ == '__main__':
    words = sys.argv[1:]
    word_list = rearrange(words)
    print(word_list)
    