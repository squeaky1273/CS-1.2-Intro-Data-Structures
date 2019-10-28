import sys
from random import choice

def list_of_lists(word_list):
    """list of lists"""
    histogram = []
    for words in word_list:
        if words in histogram:
            word_index = histogram.index(words)
            histogram[word_index + 1] += 1
        else:
            histogram.append(words)
            histogram.append(1)
    return histogram

def dictionary(word_list):
    """dictionary"""
    histogram = {}
    for words in word_list:
        if words in histogram:
            histogram[words] += 1
        else:
            histogram[words] = 1
    return histogram

def tuples(word_list):
    """list of tuples"""
    histogram = [] 
    for words in word_list:
        if words in histogram:
            histogram[words] += 1
        else:
            histogram.append((words, 1))
    return histogram

#def list_of_counts():
    #list of counts
    #histogram = []
    #return histogram

def histogram(content):
    """Writes histograms of reoccuring words"""
    f = open("text.txt", "r")
    word_list = f.read().split()
    #histogram = list_of_lists(word_list)
    histogram = tuples(word_list)
    #histogram = dictionary(word_list)
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
    print(histogram)