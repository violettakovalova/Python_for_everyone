"""
Exercise 6.3: Encapsulate this code in a function named count, and generalize
it so that it accepts the string and the letter as arguments.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

elefante
'e' - ?
"""

def countt():
    word = 'elefanteee'
    letter = 'e'
    counter = 0
    for i in word:
        if i == letter:
            counter = counter + 1
    print(counter)
#countt()



def count(word, letter):
    counter = 0
    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)
input_word = input('Enter the word: ')
input_letter = input('Enter the letter: ')
count(input_word, input_letter)
