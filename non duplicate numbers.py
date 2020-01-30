x=int(input('enter first number'))
y=int(input('enter second number'))
z=int(input('enter third number'))

sum1=x+y+z
if x !=y and x !=z:
    sum2+=x
elif y !=x and y !=z:
    sum2+=y

elif z !=x and z !=y:
    sum2+=z

print('sum of the non duplicate numbers',sum2)
