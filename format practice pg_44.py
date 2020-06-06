hours=eval(input("Please enter the number of hours you worked:"))
rate=eval(input("Please enter you hourly rate:"))
total=hours*rate
print("You earned $" + format(total,".2f"),'for',format(hours,'.1f'),
      'hours of work at $'+format(rate,'.2f')+'/hour.')
#there are other ways to format, but the last line uses the way taught in class
#used concatenation to remove the space between cents and /hour
