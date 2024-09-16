#1.5 rate
#print('Chapter 3 - Exercise 1')
#1.5 rate when over 40 hours
#Hours 40*rate+hours+15
def pay():
    hours=int(input('Enter hours: '))
    rate=int(input('Enter rate: '))
    if (hours > 40):
        hours_ot=hours-40
        hours=hours-hours_ot
        pay=hours*rate+hours_ot*rate*1.5
        print(pay)
    else:
        pay=hours*rate
        print(pay)
#pay()
