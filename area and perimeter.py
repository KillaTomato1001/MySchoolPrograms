radius=float(input('enter radius of circle'))
print('1.calculate area')
print('2.calculate perimeter')

choice=int(input('enter your choice'))
if choice==1:
    area=3.1459*radius*radius
    print(area)

else:
    perimeter=3.1459*radius*2
    print(perimeter)
