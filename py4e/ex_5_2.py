"""
Exercise 5.1: Write another program that prompts for a list of numbers as
above and at the end prints out both the maximum and minimum of the numbers
instead of the average.
"""

def exercise():
    max = None
    min = None
    while True:
        value = input('Enter a number: ')
        if value == 'done':
            break
        try:
            f_value = float(value)
        except ValueError:
            print('Invalid input')
            continue
        if max == None:
            max=f_value
        elif f_value > max:
            max = f_value
        if min == None:
            min = f_value
        elif f_value < min:
            min = f_value
    print('Maximum:',max,'Minimum:',min)
exercise()

"""
    f_value = 1
    max = 1 f_value
    min = 1 f_value

    f_value = 6
        max = 1 --- 6
        min = 1

            f_value = -1
                max = 6
                min = 1 -----  -1

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
