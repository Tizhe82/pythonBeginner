# default dictionary is dictionary subclass which calls a factory 
#  fuction to supply missing values.
from collections import defaultdict

d = defaultdict(int)

d[1] = 'python'
d[2] = 'edureka'
print(d[3])

a = {1: 'python', 2: 'edureka'}
print(a[3 ])