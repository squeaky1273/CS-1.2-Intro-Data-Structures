import sys

def sentence(number):
    """Create sentences from the provided words"""
    f = open('/usr/share/dict/words', 'r')
    word_list = f.readlines()
    f.close()
    sentence = []
    for words in word_list:
        sentence.append(words)
    return sentence

if __name__ == "__main__":
    number = sys.argv[1]
    sentence(number)