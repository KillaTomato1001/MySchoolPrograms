print('enter five numbers')
a=float(input('enter number'))
b=float(input('enter number'))
c=float(input('enter number'))
d=float(input('enter number'))
e=float(input('enter number'))
divisor=float(input('enter divisor'))
count=0
print('multiples of',divisor,'are:')
rem=a%divisor
if rem==0:
    print(a,sep='')
    count+=1
rem=b%divisor
if rem==0:
    print(b,sep='')
    count+=1
rem=c%divisor
if rem==0:
    print(c,sep='')
    count+=1
rem=d%divisor
if rem==0:
    print(d,sep='')
    count+=1
rem==e%divisor
if rem==0:
    print(e,sep='')
    count+=1
print()
print(count,'multiples of',divisor,'found')




