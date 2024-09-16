
"""
Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two paramteters (hours and
rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

def computepay(hours, rate):
    try:
        hours=float(hours)
        rate=float(rate)
    except ValueError:
        return 'Error: Please enter numeric input'
    if (hours > 40):
        pay=40*rate+(hours-40)*rate*1.5
    else:
        pay=hours*rate
    return pay
input_hours=input('Enter Hours: ')
input_rate=input('Enter Rate: ')
pay=computepay(input_hours, input_rate)
print('Pay: ', pay)
