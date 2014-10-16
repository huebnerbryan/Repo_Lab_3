## Name: Bryan Huebner
## Date: 15 October 2014
## Class: T_GIS 501 
## Description: Script written for renaming '.txt' file extension.


import os    # import operating system module

path = ('E:\\GIS_501\\Labs\\Lab_3\\text_files\\')    # set the input file path 
newpath = ('E:\\GIS_501\\Labs\\Lab_3\\text_file_changed\\') 
if not os.path.isdir(newpath):
    os.makedirs(newpath)


for root, dirs, files in os.walk(path):    # create the loop for selecting the files to changed
    
    for fil in files:    

        fil = fil.lower()    # make file names lowercase

        filsec = fil.split('.')    # split file name from file type
        

        if filsec[1] == 'txt':    # determine file type
                        
            os.rename(path + fil, newpath + "file_" + fil + '.txt')    # set for file name change
            
        else:

            os.rename(path + fil, newpath + "file_" + filsec[0] + '.txt')    # set for file type change
            

## Successful operation


## This script was developed through contributions and assistance from online tutorials, stackoverflow.com,
## and help from a fellow student (Samuel Leonard) 
