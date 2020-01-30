import math
l = int(input('enter lower input'))
x = l
while x >= l:
    y = str(x)
    sum1 = 0
    for i in y:
        num = int(i)
        f = math.factorial(num)
        sum1=sum1+f
    if sum1==x:
        print(x)
    else:
        pass
    x = x + 1
