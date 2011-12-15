from math import *
from random import *

# Parameters START

# numSegments = 10
# wavynessOffset = 0.1
# wavy = 0.1
# height = 1
# swing = 3
# bushiness = 1

# Parameters END

for i in range(int(numSegments)):
    r = 1.0 * i / numSegments
    pic("segment", x=10 * sin(wavynessOffset + wavy * r)*swing, y= r*30 *height )

for i in range(int(10 * bushiness)):
    pic("longleaf", x= randrange(-50, 50), y = randrange(-50, 50))


