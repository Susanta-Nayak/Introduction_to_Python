ans='ERROR'
n=int(input('Please enter a number between 1 and 30'))
if n>=1 and n<11:
    ans='red'
if n>=11 and n<21:
    ans='blue'
if n>=21 and n<31:
    ans='green'
print('The color is',ans+'!')
