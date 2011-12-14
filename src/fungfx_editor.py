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

editedParameter = 0
parameters = ["seed", "height", "bushiness"]
parameterValues = {"height": 0.5, "bushiness": 0.3}

editedGfx = fungfx.FunGfx()

editedGfx.load(fileName)


def changeParamValue(paramNum, delta):
    value = 0
    param = parameters[paramNum]
    if (param in parameterValues):
        value = parameterValues[param]
    value += delta
    #if value > 1: value = 1
    #if value < 0: value = 0
    parameterValues[param] = value    

def changeEditedParameter(delta):
    global editedParameter
    editedParameter += delta
    if editedParameter < 0: editedParameter = len(parameters) - 1
    elif editedParameter >= len(parameters): editedParameter = 0


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

    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[K_RIGHT]:
        changeParamValue(editedParameter, 0.1)
    if pressedKeys[K_LEFT]:
        changeParamValue(editedParameter, -0.1)

 
    screen.fill((0,0,0))

    textY = 30
    for param in parameters:
        value = 0
        if param in parameterValues: value = parameterValues[param]
        editedGfx.setParam(param, value)
        color = (128, 128, 128)
        if param == parameters[editedParameter]: color = (255, 255, 255)
        drawText(screen, (30, textY), param + ": " + str(value), color)
        textY += 30
        
    editedGfx.draw(screen, 200, 200)

    pygame.display.flip()

screen.fill((0,0,0))
drawText(screen, (screen.get_rect().centerx / 2, screen.get_rect().centery), "Closing down editor...")
pygame.display.flip()
pygame.quit ()

