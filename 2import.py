'''
How to import modules and packages
'''

# First, use other modules using 'import'
import math
print(math.sqrt(4.0))

# Can name the module using 'as'
import math as m
print(m.sqrt(4.0))

# Get exact function using 'from ... import ...'
from math import sqrt
print(sqrt(4.0))

# Get exact function using 'from ... import ...'
from math import sqrt as s
print(s(4.0))

# Can get all methods using 'from ... import *'
from math import *
print(s(4))
print(pi)
