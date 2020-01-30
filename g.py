x=str(input('enter a sequence of characters'))
w=''
i = 0
for i in x:
    w = i+w
    if x == w:
        print(x, 'is a palindrome')
        break
else:
    print(x, 'is not a palindrome')
    print('the reverse of',x,'is',''.join(reversed(x)))
