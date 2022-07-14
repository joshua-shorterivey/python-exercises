## Exercises
# ### Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# #### Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
#
#function defines single parameter, input, and will return boolean value
def is_two(input):
    #takes in input and returns a boolean based on if the input matches the stated values
    return input == 2 or input == '2'
print(is_two('b'))
print(is_two('two'))
print(is_two(2))
print(is_two('2'))

# #### Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
#function defines single parameter, str_to_check. returns boolean
def is_vowel (str_to_check):
    #returns result of check for membership in list of *vowels*
    return str_to_check.lower() in list('aeiou')
print(is_vowel('b'))
print(is_vowel('e'))

# #### Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# 
#function defines a single parameter, str_to_check, that is a string, and returns boolean value
def is_consonant(str_to_check):
    #returns the result of checking the argument passed into is_vowel() function for True/False status
    return is_vowel(str_to_check) == False
print(is_consonant('b'))
print(is_consonant('e'))

# #### Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# 
#function defines a single parameter, word, that is a string, and returns a string value
def capitalize_cons(word):
    # check character at zero index of parameter using is_consonant() function
    if is_consonant(word[0]):
        # returns parameter using str.capitalize() method
        return word.capitalize()
    # default function behaviour
    return word
print(capitalize_cons('accepts'))
print(capitalize_cons('string'))


# #### Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
# 
# function defines two parameters, tip_percent and bill_total, and will return their product after multiplication
def calculate_tip(tip_percent, bill_total):
    # returns product of multiplying both parameters together
    return tip_percent * bill_total
print(calculate_tip(.15, 75))

# #### Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
# 
# function defines two parameters, original_price and discount. returns new value after arithmetic manipulation 
def apply_discount(original_price, discount):
    # takes original price and multiplies it by the discount subtracted from 1
    # assumes discount is entered as a decimal value between 0 and 1
    return original_price * (1 - discount)
print(apply_discount(150, .25))

# #### Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
# function defines single parameter, str_num. returns integer value 
def handle_commas(str_num):
    # declares str_num as copy of str_num with commas replaced by empty string values
    str_num = str_num.replace(',' , '')
    # returns str_num cast as an int
    return int(str_num)
print(handle_commas('1,000'))

# #### Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
# function defines single parameter, numerical_grade, that is a number. will return string value 
def get_letter_grade(numerical_grade):
        # check for parameter membership in given range
    if numerical_grade in range(88, 101):
        # if in range declare and assign variable letter 
        letter = 'A'
    # check for parameter membership in given range
    elif numerical_grade in range(80, 88):
        # if in range declare and assign variable letter
        letter = 'B'
    # check for parameter membership in given range
    elif numerical_grade in range(67, 80):
        # if in range declare and assign variable letter
        letter = 'C'
    # check for parameter membership in given range
    elif numerical_grade in range(60, 67):
        # if in range declare and assign variable letter
        letter = 'D'
    # catch all condition for values not meeting other criteria
    else:
        # assign variable letter, ensures return value with be assigned *some* value
        letter = 'F'
    # returns variable letter  
    return letter
print(get_letter_grade(96))
print(get_letter_grade(60))

# function defines parameter, str_to_strip, that is a string. returns string value
def remove_vowels(str_to_strip):
    # initializes empty string variable
    str_copy = ''
    # iterates over characters in parameter
    for char in str_to_strip:
        # checks character status as vowel with is_vowel() function. executes if NOT a vowel 
        if is_vowel(char) == False:
            # if character not a vowel it appends the character to variable
            str_copy += char
    # returns variable initialized at start of function
    return str_copy
print(remove_vowels('pineapple'))

# #### Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# function defines parameter, string, that is a string. returns a string value
def normalize_name(string):
    # initializes empty string
    normalized = ''
    # creates copy of string with leading/trailing whitespaces removed --> case flattened --> internal whitespace replaced
    str_copy = string.strip().lower().replace(' ' , '_')
    # iterates over copy of parameter
    for char in str_copy:
            # checks characters in copy of parameter for status as alphabet or underscore character 
        if char.isalpha() == True or char == "_":
            # appends characters that meet requirements to string variable for eventual function return
            normalized += char
    # returns string variable previously initialized
    return normalized
print(normalize_name('        %First Name '))
print(normalize_name('   Joshua Shorter-Ivey'))

# #### Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# #### cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# #### cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# function defines parameter, num_list, that is a list of numbers. will return list of numbers
def cumulative_sum(num_list):
    # initializes list with first member being value at zero index of parameter
    new_list = [num_list[0]]
    # enumerates(?) over a version of the parameter that has been sliced starting at index one
    for idx, num in enumerate(num_list[1:]):
        # appends sum of num from parameter and the value at the sharing the same index in new_list
        new_list.append(num + new_list[idx])
    # returns list of new values
    return new_list

print(cumulative_sum([1,1,1]))
print(cumulative_sum([1,2,3,4]))

# function defines parameter, time_str, a string. returns a string
def twelveto24 (time_str):
    # initializes a string value to create default for return. is sliced version of parameter with leading zero
    time_num = f'0{time_str[:-2]}'
    # checks *trailing* characters of parameter for equality with 'pm'
    if time_str[-2:] == 'pm':
        # assigns new string value to time_num that is result of slicing and converting portions of parameter
        time_num = f'{int(time_str[:-5]) + 12}{time_str[-5:-2]}'
    # returns completed string value 
    return time_num

print(twelveto24('4:30pm'))
print(twelveto24('10:30pm'))
print(twelveto24('4:30am'))

def twentyfour_to_twelve(twentyfour_time):
    """
    Converts 24-hour time given as a string value into 12-hour time
    
    Args: 
    
    twentyfour_time: the time to be converted
    
    Returns:
    
    The result of the conversion process
    """
    
    new_time = twentyfour_time + 'am'
    if int(twentyfour_time[:-3]) > 12:
        new_time = f'{int(twentyfour_time[:-3]) - 12}{twentyfour_time[-3:]}pm'
    return new_time

print(twentyfour_to_twelve('13:40'))
print(twentyfour_to_twelve('9:00'))

# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
sheet_col_names = []
def col_index(col_name):
    """
    Searches for inclusion of given string in list of strings
    
    Args:
    
    col_name: the string value to search for
    
    Returns:
    The list index value of a string matching the search term
    """
    for idx, name in sheet_col_names:
        if name == col_name:
            return idx
    return 'No Match'