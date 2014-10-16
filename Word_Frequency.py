## Name: Bryan Huebner
## Date: 15 October 2014
## Class: T_GIS 501
## Description: Script written to determine word frequency in text file.


import operator    # import module
 
 
file_path = 'E:\\GIS_501\\Labs\\Lab_3\\HP_Lovecraft.txt'    # set file path
Lovecraft = open(file_path)    # open file
word_list = Lovecraft.read()    # set to read the (entire) text file

def clean_list():    # defining the function word list
    clean_list = word_list.lower().split()    # method to 'split' lowercase words
    words_list = []    # contain total list
    for word in clean_list:    
        symbols = "1234567890!@#$%^&*()_+{}|:\"<>?-=[]\;\',./"    # removing symbols
        for i in range(0, len(symbols)):    # setting range for the length of each word
            word = word.replace(symbols[i], "") # replace symbols with a "space"
        if len(word) > 0:    # set length of word to be greater than '0' characters
            words_list.append(word)    # add words to word list
    build_dictionary(words_list)

def build_dictionary(words_list):    # defining the function for word dictionary
    word_count = {}
    for word in words_list:    # begin loop for counting words 
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):    # loop for sorting words
        print(key, value)

clean_list()
        

## Successful operation 


## This script was developed through contributions and assistance from online tutorials, stackoverflow.com,
## and help from a fellow student (Samuel Leonard) 
 

 

