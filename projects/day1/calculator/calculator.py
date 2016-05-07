#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Calculator Project

A basic calculator.

Bloomberg Coding Workshop 2016
"""

# Print choices for user
print ''
print 'Choose an operation: '
print '1. Add'
print '2. Subtract'
print '3. Multiply'
print '4. Divide'

# Get inputs from user
operation = int(raw_input('Choose an operation (1/2/3/4): '))
num1 = int(raw_input('Enter a number: '))
num2 = int(raw_input('Enter a number: '))

# Calculate and print solution
print '--------------------------'
if operation == 1:
    print num1, '+', num2, '=', num1 + num2
elif operation == 2:
    print num1, '-', num2, '=', num1 - num2
elif operation == 3:
    print num1, '*', num2, '=', num1 * num2     
elif operation == 4 and num2 > 0:
    print num1, '/', num2, '=', float(num1) / num2
else:
    print 'Invalid Input'