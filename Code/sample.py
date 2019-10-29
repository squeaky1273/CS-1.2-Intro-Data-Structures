import histogram
import sys
import random

def sample_by_frequency(histogram):
    """Returns a single word at random 
    from the provided words/text"""
    word_list = open("text.txt", "r") #Open text file
    words = list(histogram) #Get the list of lists from the histogram
    word_index = random.randint(0, len(words) - 1) #Randomly choose a word from the list
    word_list = words[word_index]
    return word_list
    
if __name__ == "__main__":
    histogram = histogram.histogram(sys.argv[1])
    print(sample_by_frequency(histogram))