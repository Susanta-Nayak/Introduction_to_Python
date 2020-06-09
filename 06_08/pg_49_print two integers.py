'''
#write a program that inputs two different integers
one=eval(input('Please enter an integer'))
two=eval(input('Please enter a different integer'))
if one>two:
    print(one)
else:
    print(two)

#write a program that prints the largest of three integers
f=int(input('Enter first number:'))
s=int(input('Enter second number:'))
t=int(input('Enter third number:'))
if f>s:
    if f>t:
        print(f)
    else:
        print(t)
else:
    if s>t:
        print(s)
    else:
        print(t)
'''
#alternate way to write program that prints the largest of three integers
f=int(input('Enter first number:'))
s=int(input('Enter second number:'))
t=int(input('Enter third number:'))
if f>s and f>t:
    print(f)
if s>t and s>f:
    print(s)
if t>f and t>s:
    print(t)
    
    
