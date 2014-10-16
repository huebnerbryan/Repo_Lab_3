## Name: Bryan Huebner
## Date: 15 October 2014
## Class: T_GIS 501 
## Description: Script for counting words in a text file.


Lab_3_text = open('E:\\GIS_501\\Labs\\Lab_3\\GIS_is_the_best.txt')    # open path
file_list = Lab_3_text.read()   # read text file

system_count, science_count, total_words = 0,0,0    # words to be counted

for word in file_list.split(' '):    # loop for separating spaces between words
    if word.lower() == 'systems':    # setting count for 'systems'   
        system_count = system_count + 1
        
    elif word.lower() == 'science':    # setting count for 'science'
        science_count = science_count + 1
        
    else:
        total_words = total_words + 1    # setting count for total words

total_words = total_words + science_count + system_count    # combines all words for total count

print total_words    # total word count

print system_count    # total 'system' word count

print science_count    # total 'science' word count

Lab_3_text.close()    # close file


## Successful operation


## This script was developed through contributions and assistance from online tutorials, stackoverflow.com,
## and help from a fellow student (Samuel Leonard) 
