#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         5/8/2021
# Description:  Use Turtle Graphics to illustrate the city life.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

import turtle
from drawing_procedures import *


# Set the window
screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor(231, 230, 231)
screen.title('Share of Gold Medals in Tokyo Olympics, 2 August 2021')
turtle.setup(width = 750, height = 600)

# title
text = turtle.Turtle()
text.shape('turtle')
text.color('black')
move_turtle(text, 0, 245)
text.write('Share of Gold Medals in Tokyo Olympics', \
           font = ('Courier', 20, 'bold'), align = 'center')
move_turtle(text, 0, 215)
text.write('2 August 2021', font = ('Courier', 17, 'bold'), align = 'center')
text.hideturtle()

# pie
pie = turtle.Turtle()
set_turtle(pie, (231, 230, 231), 'light grey')
move_turtle(pie, -125, -280)
pie.begin_fill()
pie.circle(230)
pie.end_fill()

# Netherlands
move_turtle(pie, -125, -50)
pie.color((153, 115, 1), (153, 115, 1))
pie.begin_fill()
pie.lt(90)
pie.fd(230)
pie.lt(90)
pie.circle(230, 10.8)
pie.lt(90)
pie.fd(230)
pie.end_fill()

# The remaining segments (9, excluding Netherlands)
# Calculated by diving the # gold medals by 360%
degree = [
    10.8, 18, 18,
    32.4, 36, 39.6,
    50.4, 61.2, 82.8
    ]

colour = [
    (98, 98, 99), (158, 72, 13), (38, 69, 121),
    (113, 173, 71), (90, 155, 213), (254, 193, 0),
    (164, 165, 164), (237, 124, 48), (68, 114, 196)
    ]

# Create a loop to draw 9 segments one after another
count = 0
for i in degree:
    # Create a loop to iterate through the list of colours as each segment is drawn
    drawing = True
    while count <= 8 and drawing:   
        if count == count:
            pie.color(colour[count], colour[count])
        count += 1
        drawing = False
    # Call the function to draw the segments with corresponding calculated degrees
    segment(pie, i)
pie.hideturtle()

"""
  Call the functions to draw the labels.
  The three args are: x- and- y- coordinates and the %.
  The percentage is achieved by diving the degree by 360%.
"""

##Netherlands
label(-156, 120, '3%')
##Italy
label(-192, 110, '3%')
##S_Korea
label(-230, 90, '5%')
##France
label(-280, 55, '5%')
##G_Britain
label(-300, -20, '9%')
##ROC
label(-300, -125, '10%')
##Australia
label(-250, -220, '11%')
##Japan
label(-120, -235, '14%')
##USA
label(15, -130, '17%')
##China
label(-35, 70, '23%')

# legend_boder
boder = turtle.Turtle()
set_turtle(boder, '#F0F0F0', '#F0F0F0')
boder.begin_fill()
move_turtle(boder, 170, 140)
for _ in range (2):
    boder.fd(180)
    boder.lt(-90)
    boder.fd(365)
    boder.lt(-90)
boder.lt(90)
boder.end_fill()
boder.hideturtle()

"""
  Call the functions to write the country names.
  The three args are: colour, y coordinate and the country name.
"""

# Call the functions to write the country names
# colour, y coordinate of the legend of each country and its name
country(colour[8], 120, 'China')
country(colour[7], 85, 'USA')
country(colour[6], 50, 'Japan')
country(colour[5], 15, 'Australia')
country(colour[4], -20, 'ROC')
country(colour[3], -55, 'G. Britain')
country(colour[2], -90, 'France')
country(colour[1], -125, 'S. Korea')
country(colour[0], -160, 'Italy')
country((153, 115, 1), -195, 'Netherlands')
