# Conditional Basics
# prompt the user for a day of the week, print out whether the day is Monday or not
def is_monday():
    """
    Result of user input compared to string 'monday'
    
    Parameters
    ----------
    None
  
    Returns
    -------
    bool
        The result of comparing user input to monday
    
    """
    
    # assign user input to variable for later comparison
    today = input('What is today? ')
    if today.lower() == 'monday' :
        return print( f'It certainly is {today.capitalize}!') 
    return input('Try Again (ex: Tuesday):' )

#is_monday()

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
def is_weekend():
    day = input('What is today? ')
    if day.capitalize in ('Saturday', 'Sunday'):
        return 'It\'s the Weekend!'
    elif day.capitalize in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
        return 'Still a Weekday' 
    return input('Say Again? (Ex: Wednesday) ')
#is_weekend()

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
i = 100
while (i > -10):
    print(f'{i}\n')
    i -=5


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
print(f'{i}\n')
while (i < 1000000):
    i **= 2
    if i < 1000000:
        print(f'{i}\n')

# Write a loop that uses print to create the output shown below.
i = 100
while (i > 5):
    print(f'{i}')
    i -= 5

# For Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
i = 1
factor = int(input('What number do you want the table for? '))
while (i <= 10):
    print(f'{factor} x {i} = {factor * i}\n')
    i += 1

# Create a for loop that uses print to create the output shown below.
i = 1
while (i <= 9):
    print(f'{str(i) * i}')
    i += 1
        
# break and continue
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
number_to_skip = 'start'

while (number_to_skip):
    number_to_skip = input('Please enter an odd integer between 1 and 50: ')
    if (number_to_skip.isdigit() == True) and (int(number_to_skip) <= 50) and ((int(number_to_skip) % 2) == 1) :
        print(f'Number to skip is: {number_to_skip}\n')
        number_to_skip = int(number_to_skip)
        break

for i in range(1, 50, 2):
    if i == number_to_skip:
        print(f'Yikes! Skipping number: {i}')
        continue
    print(f'Here is an odd number: {i}')
              
# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
user_input = ''

while (user_input.isdigit() == False):
    user_input = input('Enter a positive integer: ')
    if user_input.isdigit():
        if int(user_input) > 0:
            user_input = int(user_input)
            break

for i in range(0, user_input + 1):
    print(i)

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
user_input = -1

while (user_input):
    user_input = input('Pick a positive integer: ')
    if int(user_input) > 0:
        user_input = int(user_input)
        break

for i in range(user_input, 0, -1):
    print(i)

# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
    # Write a program that prints the numbers from 1 to 100.
    # For multiples of three print "Fizz" instead of the number
    # For the multiples of five print "Buzz".
    # For numbers which are multiples of both three and five print "FizzBuzz".
for i in range (1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        print ('FizzBuzz')
    elif (i % 3 == 0):
        print('Fizz')
    elif (i % 5 == 0):
        print('Buzz')
    else:
        print(i)

# Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Bonus: Research python's format string specifiers to align the table
keep_going = 'y'
while (keep_going == 'y'):
    limit = int(input('What number would you like to go up to? '))
    #limit = int(limit)

    print('\nHere is your table!\n\nnumber | squared | cubed\n------ | ------- | -----')
    for i in range (1, limit + 1):
        print(f'{i:<6} | {i ** 2:<7} | {i ** 3:<6}')
    keep_going = input('Would you like to continue with another number? (y or n) ')
    if keep_going == 'n':
        print('Goodbye!')
        break


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
# Bonus - Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
still_grading = 'y'
numerical_grade = ' '
while (still_grading != 'n') :
    while numerical_grade.isdigit() != True:
        numerical_grade = input('Please enter a numerical grade 0 - 100 (ex: 89): ')
    
    numerical_grade = int(numerical_grade)
    if numerical_grade in range(88, 101):
        print('A')
    elif numerical_grade in range(80, 88):
        print('B')
    elif numerical_grade in range(67, 80):
        print('C')
    elif numerical_grade in range(60, 67):
        print('D')
    elif numerical_grade in range(0, 60):
        print('F')
    
    numerical_grade = ' '
    still_grading = input('\nStill Grading? (y or n) ')


# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
book1 = dict(title= 'Black Against Empire', author='Joshua Bloom', genre='History')
book2 = dict(title= 'Pre-Suasion', author='Robert Cialdini', genre='Philosophy')
book3 = dict(title= 'A People\'s History of the United States', author='Howard Zinn', genre='History')
book4 = dict(title= 'An Indigenous Peoples\' History of the United States', author='Roxanne Dunbar-Ortiz', genre='History')
book5 = dict(title= 'Destructive Creation', author='Mark R. Wilson', genre='History')
book6 = dict(title= 'When Small States Make Big Leaps', author='Darius Ornston', genre='History')
book7 = dict(title= 'The Denial Of Death', author='Ernest Becker', genre='Philosophy')
book8 = dict(title= 'Principles: Life and Work', author='Ray Diallo', genre='Philosophy')
    
library = (book1, book2, book3, book4, book5, book6, book7, book8)
for book in library:
    print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
search_genre = input('\nPlease enter a genre to search for: ')
for book in library:
    if book['genre'] == search_genre:
        print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")