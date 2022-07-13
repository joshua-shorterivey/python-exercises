# Conditional Basics
# prompt the user for a day of the week, print out whether the day is Monday or not
def is_monday():
    today = input('What is today? ')
    if today == 'Monday' :
        return print( f'It certainly is {today}!') 
    return input('Try Again (ex: Tuesday):' )
is_monday()

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
def is_weekend():
    day = input('What is today? ')
    if day in ('Saturday', 'Sunday'):
        return 'It\'s the Weekend!'
    elif day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
        return 'Still a Weekday' 
    return input('Say Again? (Ex: Wednesday) ')
is_weekend()

# create variables and make up values for
# the number of hours worked in one week
work_hours = 37.5
# the hourly rate
hourly_rate = 25
# how much the week's paycheck will be
gross_pay = work_hours * hourly_rate 

# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
def pay_calc(hours, rate):
    if hours > 40:
        return (hours * rate) + ((hours % 40) * (rate * 1.5))
    return hours * rate

# Loop Basics
# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while (i <= 15):
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while (i < 100):
    i += 2
    print(f'{i}\n')
# Alter your loop to count backwards by 5's from 100 to -10.
i = 105
while (i > -10):
    i -=5
    print(f'{i}\n')
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

# Write a loop that uses print to create the output shown below.

# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# Create a for loop that uses print to create the output shown below.

# break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# Bonus: Research python's format string specifiers to align the table

# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus

# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.