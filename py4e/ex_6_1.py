"""
Exercise 6.1: Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

def reverse ():
    data = 'banana'
    index = len(data) - 1
    while index >= 0:
        answer = data[index]
        print(answer)
        index = index - 1
reverse ()
