# Code based on http://www.pygame.org/wiki/LazyImageLoading?parent=CookBook

import pygame
import weakref
 
class ResourceManager(object):
    def __init__(self, basedir, loader):
        self.__dict__.update(dict(
            cache = weakref.WeakValueDictionary(),
            loader = loader,
            basedir = basedir
        ))
       
    def get(self, name):
        try:
            img = self.cache[name]
        except KeyError:
            img = self.loader(self.basedir + name + ".png")
            self.cache[name] = img 
        return img
        
    
class ImageManager(ResourceManager):
    def __init__(self, basedir):
        ResourceManager.__init__(self, basedir, pygame.image.load)
        
        
imageManager = ImageManager("assets/images/")
        
