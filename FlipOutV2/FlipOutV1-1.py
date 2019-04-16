##Nathan Hinton
#This is a clone of flip out.
##Goals:
# 1) Larger game board

#Setup Vars:

(widths, heights) = (20, 20)
size = 20
BLACK = (0, 0, 0)

#File paths:
red = './Red.png'
blue = './Blue.png'
green = './Green.png'
yellow = './Yellow.png'

#Round the game size to be nice:
(width, height) = (widths*size, heights*size)

import pygame
from random import choice
from time import sleep

choices = ['red', 'blue', 'green', 'yellow']

class Chip:
    def __init__(self, surface, posx, posy, color):
        self.x = posx
        self.y = posy
        if color == 'red':
            self.color = red
        elif color == 'blue':
            self.color = blue
        elif color == 'green':
            self.color = green
        elif color == 'yellow':
            self.color = yellow
        else:
            print("!INVALID COLOR OPTION!")
        self.image = pygame.image.load(self.color).convert_alpha()
        surface.blit(self.image, (self.x*size, self.y*size))
    def drop(self):
        pass#if a peice is not under it then fall down until peice is under
    def score(self):
        pass
    def update(self, pos, color):
        pass#This is for checking where the mouse was clicked and if this needs to drop/dissapear.


#Square size = size
def drawBG():
    for x in range(int(width/size)):
        pygame.draw.line(screen, BLACK, (x*size, 0), (x*size, height), 3)
        for y in range(int(height/size)):
            pygame.draw.line(screen, BLACK, (0, y*size), (width, y*size), 3)

##Setup the game:
pygame.init()
pygame.display.set_caption('FlipOut 2.0')
screen = pygame.display.set_mode((width, height))
background_color = (255,255,255)
screen.fill(background_color)
pygame.display.flip()
##drawBG()
##pygame.display.flip()

chips = []
for posx in range(widths):
    for posy in range(heights):
        chips.append(Chip(screen, posx, posy, choice(choices)))

pygame.display.flip()    

def getNextTo(chips, pos):
    x, y = pos
    closeChips = []
    for chip in chips:
        if (chip.x, chip.y) == (x+1, y):
            closeChips.append(chip)
        elif (chip.x, chip.y) == (x-1, y):
            closeChips.append(chip)
        elif (chip.x, chip.y) == (x, y+1):
            closeChips.append(chip)
        elif (chip.x, chip.y) == (x, y-1):
            closeChips.append(chip)
        else:
            pass
    return closeChips

#Main Loop:
running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            #Start the function for when chip is clisked:
            chipsToDissapear = []
            pos = pygame.mouse.get_pos()
            pos = int(pos[0]/size), int(pos[1]/size)
            for chip in chips:#Figure out which chip clicked and where
                if (chip.x, chip.y) == pos:
                    print(pos)
                    clickedChip = chip
                    color = chip.color
                    chipsToDissapear.append(clickedChip)
                    break
            #Figure out if the ones next to it are the same color.
            check = True
            closeChips = getNextTo(chips, pos)
            for chip in closeChips:
                if chip in chipsToDissapear:
                    pass
                elif chip.color == color:
                    chipsToDissapear.append(chip)
                    nextItration.append(chip)
            while check == True:
                if nextIteration == []:
                    check = False
                for chip in nextIteration:
                    
                    closeChips = getNextTo(chips, pos)
                    for chip in closeChips:
                        if chip in chipsToDissapear:
                            pass
                        elif chip.color == color:
                            chipsToDissapear.append(chip)
                            nextItration.append(chip)
                        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()