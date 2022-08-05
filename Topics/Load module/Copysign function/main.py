# place `import` statement at top of the program


# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))
from math import copysign
print(copysign(x, y))