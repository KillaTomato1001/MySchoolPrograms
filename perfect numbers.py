import math
l = int(input('enter lower limit'))
y = l
while y >= l:
    x = y

    s = 0
    for a in range(1, x):
        if x % a == 0:
            s = s + a
    if s == y:
        print(y, 'is a perfect number')
    else:
        pass
    y = y + 1
else:
    print('Done')
