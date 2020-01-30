x=int(input('enter first number'))
y=int(input('enter second number'))
z=int(input('enter third number'))
min=mid=max=None
if x<y and x<z:
    if y<z:
        min,mid,max=x,y,z
    else:
        min,mid,max=x,z,y
        
        
            

