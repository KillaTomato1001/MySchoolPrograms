print('the equation of the form ax^2+bx+c')

a=int(input('input leading coefficient'))
b=int(input('input x coefficient'))
c=int(input('input constant'))
value=str(input('which value do you require'))
discriminant=b**2-4*a*c

if value=='A':
    print((-b+discriminant)/2*a)

if value=='B':
    print((-b-discriminant)/2*a)


    




