"""
Program: camper_age_input.py
Author: Sean Gilbert
Last modified: 09/06/20

This program declares the function convert_to_months.
Users are prompted for their age and the input passes into convert_to_months
The function return is the input multiplied by 12
The program prints the result
"""


def convert_to_months(years):
    months = years * 12
    return months


if __name__ == '__main__':
    age_in_years = int(input('Enter your age: '))
    age_in_months = convert_to_months(age_in_years)
    print(age_in_years, "years is", age_in_months, "months")

# This is a comment
