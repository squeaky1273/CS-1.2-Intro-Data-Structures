import sys
from random import choice

def histogram(file_name):
    """Writes histograms of reoccuring words"""
    #list of lists
    histogram = []
    for word in file_name:
    
    #dictionary
    histogram = {}
    for word in file_name:
    
    #list of tuples
    histogram = [] 
    for word in file_name:
    
    #list of counts
    #histogram = []

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
    #f = open("text.txt", "r")
    #content = f.read()
    #histogram(content)
    pass