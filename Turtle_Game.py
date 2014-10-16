## Name: Bryan Huebner
## Date: 15 October 2014
## Class: T_GIS 501
## Description: Script written to prompt a 'user' to select an integer -
## from which Turtle Graphics will draw a shape with the chosen number of sides.


from turtle import *    # import Turtle Graphics - use the '*' to import "all of Turtle Graphics
##import random

print ("This program draws shapes in a uniform pattern based on the number you select.")    # statement telling the 'user' what to expect    

num_str = input("Select the number of sides for the shape you want to draw: ")    # prompt 'user' to select a an integer

turtle = Pen()    # identify pen  
turtle.shape('turtle')    # select the drawing symbol (turtle shape)
turtle.speed ('slow')    # set speed at which turtle will draw
turtle.screen.bgcolor('#160912')    # set the background color of the drawing screen        
turtle.color ('#00D143')    # set the color of the 'turtle'

for i in range(num_str):    # loop used to generate the shape based on the interger selected by the 'user'       
    turtle.forward(50)
    turtle.left(360/num_str)


## Succesful operation


## This script was developed through contributions and assistance from online tutorials, stackoverflow.com,
## and help from a fellow student (Samuel Leonard) 




