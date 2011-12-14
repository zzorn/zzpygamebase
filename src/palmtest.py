from math import *
from random import *

for i in range(10):
    pic("segment", x=10 * sin(i/1.5)*2.4, y=i*30 *height )

for i in range(int(10 * bushiness)):
    pic("longleaf", x= randrange(-50, 50), y = randrange(-50, 50))


