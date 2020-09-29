# Sean Gilbert
# CIS 189 Fall 2020
# Module 5 Topic 2: The while Loop
# Input Validation while Loops Assignment
# Prompts user for input and adds input to list if input in correct range

cool_list = []
sentinel = 999

entry = int(input('Enter a whole number between 1 and 100, or enter 999 to stop: '))

while entry != sentinel:
    while entry not in range(1, 101):
        entry = int(input('Invalid entry. Number must be between 1 and 100. Enter 999 to stop: '))
    cool_list.append(entry)
    entry = int(input('Previous entry recorded. Enter an integer between 1 and 100: '))


for x in cool_list:
    print(x)

#Input: 5,3,67,999 Output: 5,3,67
#Input: 105,1210,5,999 Output: 5
#Input: 120,999 Output: stuck in loop
