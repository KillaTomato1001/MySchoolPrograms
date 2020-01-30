num1=int(input('enter first number'))

num2=int(input('enter second number'))
remainder=num1%num2
if remainder==0:
    print(num1,'is divisible by',num2)
else:
    print(num1,'is not divisible',num2)
