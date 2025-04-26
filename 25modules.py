# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

print(help("modules"))

import math
import math as m
from math import pi

pi 
m.pi
print(math.pi)

print(math.e ** 1)
print(math.e ** 2)

import modules

result = modules.pi
result = modules.square(3)
result = modules.cube(3)
result = modules.circumference(3)
result = modules.area(3)