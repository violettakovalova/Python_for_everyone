"""
Exercise  6.5: Take the following Python code that stores a string:

string = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted string
into a floating number.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
string = 'X-DSPAM-Confidence: 0.8475'
pos = string.find(':')
number = string[pos+1:]
f_number = float(number)
print(f_number)
