import math
x=int(input('enter principle amount'))
y=int(input('enter time period of loan'))
z=int(input('enter rate of interest'))
a=1+z/100
ci=x+(math.pow(a,y))
print(ci)
