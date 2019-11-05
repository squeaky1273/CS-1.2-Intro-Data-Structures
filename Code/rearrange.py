import random
import sys

def rearrange(words):
    """Rearrange words that are provided"""
    word_list = []
    count = 0
    while count < len(words):
        new_word = random(words)
        if new_word not in word_list: #If the new word is not already in the list, then add it to the list
            word_list.append(new_word)
            count += 1
    return (" ".join(word_list))

def reverse(words):
    """Reverse words that are provided"""
    inputWord = " ".join(words)
    output = inputWord[::-1]
    return output

if __name__ == '__main__':
    words = sys.argv[1:]
    #word_list = rearrange(words)
    #print(word_list)
    print(reverse(words))