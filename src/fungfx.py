import pygame, random, math
from pygame.locals import *

import resourcemanager


class FunGfx(object):

    def __init__(self):
        self.params = {}

    def load(self, source):
        self.source = source

    def draw(self, surface, basex, basey):
        def pic(name, x, y):
            img = resourcemanager.imageManager.get(name)
            surface.blit(img, (basex + x, basey + y))

        runtimeParams = {}
        runtimeParams.update(self.params)
        runtimeParams['basex'] = basex
        runtimeParams['basey'] = basey
        runtimeParams['surface'] = surface
        runtimeParams['pic'] = pic

        random.seed(self.getParam("seed", 42))

        execfile(self.source, {}, runtimeParams)       
        
    def setParam(self, paramName, paramValue):
        self.params[paramName] = paramValue
    

    def getParam(self, paramName, defaultValue):
        if paramName in self.params: return self.params[paramName]
        else: return defaultValue
                    

