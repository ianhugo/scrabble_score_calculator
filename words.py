
'''
This is a module that provides three functions:

extract_words() = takes file path as argument, 
returns a list of the words
(this file should contain allowable 3 letter Scrabble words)

calc_score() = takes a list of words as argument, 
calculates Scrabble score for each word, r
eturns a dictionary of words and their scores

sort_by_score() = sorts the words in the dictionary, by their score, 
returns sorted list of tuples of words and their scores
'''
import re

def extract_words(y):

    file_path = str(y)

    f = open(file_path, "r")

    a =[]
    for line in f:
        t = line.strip()
        #this can scale up to take more than 3 letter words
        match = re.search(r'([a-zA-Z]+)?\s\|(.*)', t)
        try:
            a.append(match[1])
        except TypeError:
            continue

    return a

def calc_score(y):

    dict1 = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}

    dict_score = {}

    for i in range(len(y)):
        for j in range(len(y[i])):
            t = dict1[(y[i][j]).lower()]
            try:
                dict_score[y[i]] += int(t)
            except KeyError:
                dict_score[y[i]] = 0
                dict_score[y[i]] += int(t)
    
    return (dict_score)

def sort_by_score(dict_score):
    sorted_dict = []
    #provide key for sort comparison, dict_score.get returns the values
    # third argument reverse = T, as want descending
    for k in sorted(dict_score, key=dict_score.get, reverse=True):
        sorted_dict.append((k, dict_score[k]))
    
    return sorted_dict