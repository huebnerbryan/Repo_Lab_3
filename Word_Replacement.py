## Name: Bryan Huebner
## Date: 15 October 2014
## Class: T_GIS 501 
## Description: Script written to replace selected words in a (.txt) text file.



Lab_3_text = open('E:\\GIS_501\\Labs\\Lab_3\\GIS_is_the_best.txt')    # open file path 

infile = open('E:\\GIS_501\\Labs\\Lab_3\\GIS_is_the_best.txt')    # select an 'infile' 

outfile = open('E:\\GIS_501\\Labs\\Lab_3\\Output_1.txt', 'w')    # select an 'outfile' 

replacements = {'Science':'Systems', 'science':'systems'}    # select the target words  

for line in infile:    # loop for replacement of word
    for src, target in replacements.iteritems():
        line = line.replace(src, target)
    outfile.write(line)

infile.close()    # close infile 

outfile.close()   # close outfile


## Successful operation


## This script was developed through contributions and assistance from online tutorials, stackoverflow.com,
## and help from a fellow student (Samuel Leonard) 
