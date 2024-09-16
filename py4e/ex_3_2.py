def pay():
    try:
        hours=int(input('Enter hours: '))
        rate=int(input('Enter rate: '))
    except:
        print('Error: Please enter numeric input')
        quit()
    if (hours > 40):
        hours_ot=hours-40
        hours=hours-hours_ot
        pay=hours*rate+hours_ot*rate*1.5
        print(pay)
    else:
        pay=hours*rate
        print(pay)
pay()
