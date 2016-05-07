# Bloomberg Coding Workshop 2016

## Calculator Project
Basic calculator

### Project Instructions
In this project, we will build a calculator that performs basic arithmetic.  The program should allow users to choose from a list of available operation (ie., addition, subtraction, etc), enter 2 operands and output the equation and solution.

### Files
Filename | Description
---|---
calculator.py | Calculator program

### External Libraries Required
None

### Key Concepts Used
- Standard I/O
- Variables
- Casting
- If-Then-Else

### Code Walkthrough

#### Printing Instructions For the User
This program will perform 1 of 4 possible operations.  The user will be able to enter a number that corresponds to the operation they want.

``` python
# Print choices for user
print ''
print 'Choose an operation: '
print '1. Add'
print '2. Subtract'
print '3. Multiply'
print '4. Divide'
```

#### User Input
The user is prompted to choose an operation entering a number between 1 and 4.  That value is stored in a variable called `operation`.  Next the user is prompted to enter the first operand, which is stored in `num1`.  Then again for `num2`.  Note, the `raw_input` function returns a `string`, regardless of what the user typed.  For example, the number 1 will be returned as '1'.  Therefore we cast each of these string values to integer before assigning them to the variables.  Reference [here](https://docs.python.org/2/library/functions.html#int).

``` python
# Get inputs from user
operation = int(raw_input('Choose an operation (1/2/3/4): '))
num1 = int(raw_input('Enter a number: '))
num2 = int(raw_input('Enter a number: '))
```

#### Perform Calculation
We use a chain of if/elif/else statements to determine which operation to perform.  If the `operation` variable holds the integers 1, 2, 3 and 4, the relevant operation is performed and the equation and result is printed.  Any other integer will result in no operation being performed and an error message being outputed to to the user.  Note: for division, we also ensure the dividend is greater than 0.

``` python
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
```

### Extending this Project
- Add more operations, such as exponentiation
- Add input validation
 - In the current program, the int casting will throw an error if the user enters a non-numeric character
 - If the user enters a number larger than what int can hold, there will be a loss of prevision
- Use string format() method to format output text