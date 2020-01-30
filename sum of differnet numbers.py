count=sum=0
ans='y'
while ans=='y':
    num=int(input('enter a number:'))
    if num<0:
        print('the enter number is below zero. Aborting!')
        break
    sum=sum+num
    count=count+1
    ans=input('want to enter more numbers (y/n)...')
else:
    print('sum  of number enter is' ,sum)
              
