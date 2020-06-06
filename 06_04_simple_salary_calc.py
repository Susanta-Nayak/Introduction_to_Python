'''
hours=float(input('Please enter the number of hours that you worked'))
rate=float(input('Please enter you hourly rate:'))
print('You earned',hours*rate,'for' ,hours,'work at',rate,'dollars/hour')
'''
hours=float(input('Please enter the number of hours that you worked'))
rate=float(input('Please enter you hourly rate:'))
print('You earned'+'$',format(hours*rate,'.2f'),'for' ,hours,'hours of work at',+'$',format(hours,'$f'),'/hour')
