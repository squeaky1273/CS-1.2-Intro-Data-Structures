import sys 
from random import choice

def dictionary(word_list): #Easy, Worst in terms of space efficiency, Fastest
    """dictionary"""
    histogram = {}
    for words in word_list: #For the words in the text file
        if words in histogram: #If the word is in the histogram,
            histogram[words] += 1  #increase the frequency numbers
        else: #Else, 
            histogram[words] = 1 #keep the word count to be 1
    return histogram #Returns the dictionary part of the histogram

def list_of_lists(word_list): #Hard, Worse than tuples in terms of space efficiency, Relatively slow
    """list of lists""" 
    histogram = []
    for words in word_list: #For the words in the text file
        if words in histogram: #If the word is in the histogram,
            word_index = histogram.index(words) #The words are added tot he index of multiples of specific words
            histogram[word_index + 1] += 1 #Adds 1 as many times as the word appears
        else:
            histogram.append(words) #Add the word to the list
            histogram.append(1) #Add the number '1' next to it for the word's frequency
    return histogram #Returns the list if lists part of the histogram

def tuples(word_list): #Harder, Better than list of lists in terms of space efficiency, Relatively slow
    """list of tuples""" #Can't change the values in a tuple, otherwise you need to create a whole new one
    histogram = [] 
    for words in word_list: #For the words in the text file
        for tuples in histogram: #For the words in the histogram
            if tuples[0] == words: #If the tuples equals the words in the text
                histogram[histogram.index(tuples)] = (words, (tuples[1] + 1)) #From the index of words, add 1 in it appears more than once
                break
        else:
            histogram.append((words, 1)) #The word will have just one for the frequency
    return histogram #Return the tuple part of the histogram

"""
def list_of_counts(word_list): #Hardest, Best in terms of space efficiency, Slowest
    #list of counts #The numbers are listed once with a list of the words that appeared that many times  ex: [(1, ['one', 'two', 'red', 'blue']) (4, ['fish'])]
    hist = histogram(word_list)
    count = {}
    return histogram
"""

def histogram(content):
    """Writes histograms of reoccuring words"""
    f = open("text.txt", "r") #Opens the text file
    #f = open(content, 'r') 
    word_list = f.read().split() #Reads the text file

    histogram = dictionary(word_list)
    #histogram = list_of_lists(word_list)
    #histogram = tuples(word_list)
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
    #histogram = histogram(sys.argv[1])
    # f = open("text.txt", "r")
    # content = f.read()
    
    content = "text.txt"
    print(histogram(content))