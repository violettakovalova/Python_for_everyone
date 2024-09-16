def score():
    try:
        x=float(input('Enter the score: '))
        min_value = 0.0
        max_value = 1.0
        if (min_value <= x <= max_value):
            if (x>=0.9):
                print('A')
            elif (x>=0.8):
                print('B')
            elif (x>=0.7):
                print('C')
            elif (x>=0.6):
                print('D')
            else:
                print('F')
        else:
            print('Bad score')
    except:
        print('Bad score')
        quit()
score()

#score(perfect)
#score(10.0)
#score(0.75)
#score(0.5)

"""
Exercise 3.Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and
1.0, print a grade using the following table:
Score    Grade
>= 0.9      A
>= 0.8      B
>= 0.7      C
>= 0.6      D
< 0.6      F
~~~

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly as shown above to test the various, different
values for input.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
