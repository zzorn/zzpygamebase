import pygame, random, math
from pygame.locals import *

import resourcemanager
from paramparser import *

defaultParams = {"seed": 42}

class FunGfx(object):

    def __init__(self):
        self.params = {}

    def load(self, sourceFile):
        self.sourceFile = sourceFile
        self.readSource()

    def readSource(self):
        f = open(self.sourceFile)
        sourceText = f.read()
        f.close()

        # Include default parameters
        newParams    = defaultParams.copy()

        # Get parameters from sources        
        newParams.update(parseParams(sourceText))

        # Copy over previous values
        for p in self.params:
            if p in newParams: newParams[p] = self.params[p]

        # Update field
        self.params = newParams

    def draw(self, surface, basex, basey):

        self.readSource()

        def pic(name, x, y):
            img = resourcemanager.imageManager.get(name)
            surface.blit(img, (basex + x, basey + y))

        runtimeParams = self.params.copy()
        runtimeParams['basex'] = basex
        runtimeParams['basey'] = basey
        runtimeParams['surface'] = surface
        runtimeParams['pic'] = pic

        random.seed(self.getParam("seed", 42))

        execfile(self.sourceFile, {}, runtimeParams)       
        
    def setParam(self, paramName, paramValue):
        self.params[paramName] = paramValue
    

    def getParam(self, paramName, defaultValue):
        if paramName in self.params: return self.params[paramName]
        else: return defaultValue
                    
    def parameterNames(self):
        return self.params.keys()                
                    
    def getParams(self):
        return self.params                   

    def changeParamValue(self, param, delta):
        value = 0
        if (param in self.params):
            value = self.params[param]
            
        if abs(value) > 1: delta *= abs(value)
            
        value += delta
        #if value > 1: value = 1
        #if value < 0: value = 0
        self.params[param] = value    


