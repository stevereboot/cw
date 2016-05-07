#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Hello World Project

Printing, variables and interacting with users.

Bloomberg Coding Workshop 2016
"""

# Print to screen
print 'Hello World'

# Print with variable
name = 'Steve'
print 'Hello ' + name

# Ask user to enter name, and assign it to variable
name = raw_input('Enter your name: ')
print 'Hello ' + name

# Another way to print with variable
first_name = raw_input('Enter your first name: ')
last_name = raw_input('Enter your last name: ')
print 'Hello {} {}'.format(first_name, last_name)

# Another way to print with position numbers
print 'Or is it {1}, {0}'.format(first_name, last_name)