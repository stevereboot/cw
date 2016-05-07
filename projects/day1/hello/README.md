# Bloomberg Coding Workshop 2016

## Hello World Project
Printing, variables and interacting with users

### Project Instructions
In this project, we will learn how to interact with users by displaying messages on the screen and taking their input.  We will also learn how to use `variables` to hold data and make your code more efficient.  For this project, the instructors will walk you through each step.

### Files
Filename | Description
---|---
hello.py | Script to print hello

### External Libraries Required
None

### Key Concepts Used
- Standard I/O
- Variables
- String Formatting

### Code Walkthrough

#### Outputing Text to the Screen
The most basic form of communication with users of your program is to display text output using python's `print` statement.  The words 'Hello World' are printed to the screen.

``` python
# Print to screen
print 'Hello World'
```

#### Variables
Variables store data, such as text, which can be used in a print statement to provide flexibility to your program.  The variable called `name` is assigned the name 'Steve'.  Then the sentence 'Hello ' with the name in `name` is printed to the screen.

``` python
# Print with variable
name = 'Steve'
print 'Hello ' + name
```

#### User Input
Another way to communicate with with your users is to ask them for input and use that input in your program.  The function `raw_input` prints 'Enter your name: ' to the screen and waits for the user to enter text.  It then assigns that text as a string to the variable `name`.  Then the sentence 'Hello ' with the user's name is printed to the screen.

``` python
# Ask user to enter name, and assign it to variable
name = raw_input('Enter your name: ')
print 'Hello ' + name
```

#### String Formatting
In the previous lines, the `name` variable is joined with the word 'Hello ' using the `+` operator.  Another way to inject variables into strings is to use the `format()` method.  Read more [here](https://docs.python.org/2/library/stdtypes.html#str.format).  The user is prompted to enter their first and last names.  Those are assigned to the variables `first_name` and `last_name`.  To form a sentence, the `format()` method takes the two name variables and replaces each `{}` with those variables in order.

``` python
# Another way to print with variable
first_name = raw_input('Enter your first name: ')
last_name = raw_input('Enter your last name: ')
print 'Hello {} {}'.format(first_name, last_name)
```

#### String Formatting with format()
In the previous line, there were two `{}` replacement fields.  And `first_name` and `last_name` were inserted into each of them in order.  To specify which `{}` is replaced with which argument, positional argument specifiers can be used.  They are zero indexed.  Here, the users first and last names are printed last name first.

``` python
# Another way to print with position numbers
print 'Or is it {1}, {0}'.format(first_name, last_name)
```

### Extending this Project
- Create an interactive program, with multiple inputs and outputs
