x = input('enter a string')
l = len(x)
i=0
for a in range(-1,-(l+1),-1):
    print(x[i],'\t',x[a])
    i+=1