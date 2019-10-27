import sys
from random import choice

def list_of_lists(word_list):
    histogram = []
    for words in word_list:
        if words in histogram:
            histogram[words] += 1
        else:
            histogram[words] = 1

def dictionary(word_list):
    #dictionary
    histogram = {}
    for words in word_list:
        if words in histogram:
            histogram[words] += 1
        else:
            histogram[words] = 1

def tuples(word_list):
    #list of tuples
    histogram = [] 
    for words in word_list:
        if words in histogram:
            histogram[words] += 1
        else:
            histogram[words] = 1

#def list_of_counts():
    #list of counts
    #histogram = []

def histogram(file_name):
    """Writes histograms of reoccuring words"""
    word_list = file_name
    #histogram = list_of_lists(word_list)
    #histogram = tuples(word_list)
    histogram = dictionary(word_list)
    return histogram

def unique_words(histogram):
    """Takes the histogram arguments"""
    count = 0
    for list in histogram:
        for index in choice(len(list)):
            if type(list[index]) is int and list[index]==1:
                count += 1

def frequency(words, histogram):
    """Returns number of times the word apppears"""
    return histogram[words]

if __name__ == "__main__":
    histogram = histogram(sys.argv[1])
    f = open("text.txt", "r")
    content = f.read()
    histogram(content)
    pass