import pygame, random, math, pygame.font
from pygame.locals import *

from pyparsing import Word, Literal, alphas
import fungfx
import resourcemanager

# Setup
pygame.init()
pygame.font.init()

size = [800, 600]
screen = pygame.display.set_mode(size)

font = pygame.font.Font(None, 32) 

pygame.display.set_caption("FunGfx Editor")

fileName = "src/palmtest.py"


editedGfx = fungfx.FunGfx()
editedGfx.load(fileName)

# Keep track of currently edited parameter
editedParameterName = ""
editedParameterNum  = 0
def changeEditedParameter(delta):
    global editedParameterName
    global editedParameterNum
    editedParameterNum += delta
    if editedParameterNum < 0: editedParameterNum = len(editedGfx.parameterNames()) - 1
    elif editedParameterNum >= len(editedGfx.parameterNames()): editedParameterNum = 0
    editedParameterName = editedGfx.parameterNames()[editedParameterNum]


def drawText(surface, pos, text, color = (128, 128, 128)):
    textPic = font.render(text, True, color, (0,0,0))
    surface.blit(textPic, pos)

# Loop
clock = pygame.time.Clock()
running  = True
while running:
 
    clock.tick(10)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
            editedGfx.load(fileName)
        elif event.type == pygame.KEYDOWN and event.key == K_UP:
            changeEditedParameter(-1)
        elif event.type == pygame.KEYDOWN and event.key == K_DOWN:
            changeEditedParameter(1)

    # Check if we are adjusting the value
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[K_RIGHT]:
        editedGfx.changeParamValue(editedParameterName, 0.1)
    if pressedKeys[K_LEFT]:
        editedGfx.changeParamValue(editedParameterName, -0.1)

 
    screen.fill((0,0,0))

    # Show parameter values, and highlight selected one
    textY = 30
    for paramName in editedGfx.parameterNames():
        value = editedGfx.getParam(paramName, 0)
        
        color = (128, 128, 128)
        if paramName == editedParameterName: color = (255, 255, 255)
        
        drawText(screen, (30, textY), paramName + ": " + "%.2f" % value, color)
        textY += 30

    # Draw gfx        
    editedGfx.draw(screen, 200, 200)

    pygame.display.flip()

# Notify about closing, as close delay is kind of long
screen.fill((0,0,0))
drawText(screen, (screen.get_rect().centerx / 2, screen.get_rect().centery), "Closing down editor...")
pygame.display.flip()

pygame.quit ()

