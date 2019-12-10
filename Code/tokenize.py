
import sys
import re

f = open('corpus.txt')
text = f.read().lower().split

def tokenize(text):
    tokens = split_on_whitespace(text)
    return tokens

def split_on_whitespace(text):
    return re.split('\s+', text)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open('corpus.txt').read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename given as argument')
