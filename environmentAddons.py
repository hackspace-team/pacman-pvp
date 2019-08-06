import pygame
from pygame.locals import *
from numpy import loadtxt

#intervalx is the width between each character in a row
#intervaly is the height between each character in a column
#intervalx= 
#intervaly= 
#below is the radius of the dot

radius= 2
count= 0
pygame.init()
screen = pygame.display.set_mode((1200,600))
width, height = (32, 32)
squares = []
circles= []
rows, columns = layout.shape
for col in range(columns):
    for row in range(rows):
        value = layout[row][col]
        if value == '%':
            pos = (columns*width, row*height)
            Square= pygame.draw.rect(pos, intervalx, intervaly)
            squares.append(Square)
        elif value == ' . '
            pos2= (columns*width, row*height)
            Dot= pygame.draw.circle(screen, (227,207,87), pos2, radius)
            circles.append(Dot)
while True:

    for Dot in circles:
        if xpos==pos2:
            count+=1
            circles.remove(Dot)
            if count== circles.length()-1:
                current_room_number+=1
                current_room=rooms[current_room_number]
                
