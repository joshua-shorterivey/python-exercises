# 99.9 --> float
# "False" --> str
# False --> bool
# '0' --> str
# 0 --> itr
# True --> bool
# 'True' --> str
# [{}] --> list
# {'a': []} --> dict

# What data type would best represent:

# A term or phrase typed into a search box? str
# If a user is logged in? bool
# A discount amount to apply to a user's shopping cart? float
# Whether or not a coupon code is valid? bool
# An email address typed into a registration form? str
# The price of a product? float
# A Matrix? list
# The email addresses collected from a registration form? str
# Information about applicants to Codeup's data science program? dict

# Question 1
# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

total_rental_price = (3 + 5 + 1) * 3 # assign result of arithmetic to variable
print(total_rental_price)

# Question 2
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

gross_pay = (400 * 6) + (380 * 4) + (350 * 10) #assign result of arithmetic to variable
print(gross_pay)

# Question 3
# # A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
# I wildly overshot what the assignment was asking for. Need to do better planning next time. 

import datetime as dt #import datetime library

# dictionaries containing values for later comparison
# used datetime timedelta object in order to facilitate arithmetic operations
ethics_101 = {'e_cap': 25, 'e_cur': 22, 'weekday': 'Thu', 'start_time': dt.timedelta(hours=13, minutes=00), 'end_time': dt.timedelta(hours=14, minutes=30)}
psyc_101 = {'e_cap': 25, 'e_cur': 24, 'weekday': 'Wed', 'start_time': dt.timedelta(hours=13, minutes=00), 'end_time': dt.timedelta(hours=14, minutes=30)}
math_1 = {'e_cap': 25, 'e_cur': 23, 'weekday': 'Mon', 'start_time': dt.timedelta(hours=13, minutes=00), 'end_time': dt.timedelta(hours=14, minutes=30)} 
eng_1b = {'e_cap': 25, 'e_cur': 15, 'weekday': 'Sat', 'start_time': dt.timedelta(hours=13, minutes=00), 'end_time': dt.timedelta(hours=14, minutes=30)} 
math_13 = {'weekday': 'Thu', 'start_time': dt.timedelta(hours=12, minutes=00), 'end_time': dt.timedelta(hours=13, minutes=30)}

student_schedule = (psyc_101, math_1, eng_1b, math_13) #creates list of dictionaries

def conflict_check(schedule, section):
    """
    Compare class (section) against others in a schedule
    
    Keyword arguments:
    schedule -- list of sections with each represented as a dictionary
    section -- the individual section being used for comparison
    """
    
    # checks to see if section is has *seats* left. returns string if True
    if section['e_cap'] == section['e_cur']:
        return 'Section full.'
    
    #iterates over schdule for comparison of weekday and time conflicts
    for item in schedule:
        if section['weekday'] == item['weekday']:
            if section['start_time'] < item['end_time'] < section['end_time']\
                or section['start_time'] < item['start_time'] < section['end_time']:
                return 'Section conflicts with current schedule.'
    
    # *default* return if all other checks passed         
    return 'Student may join.'

print (conflict_check(student_schedule, ethics_101)) #print for verification

# Question 4
# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# sets up variables for later test
customer_1 = {'purchase_count': 1, 'premium': True}
promotion_1 = {'discount': .85, 'exp_date': dt.date(2021, 12, 31)}

def apply_offer(customer, offer):
    """
    Decides whether or not to present offer to customer
    
    Keyword arguments: 
    customer -- the customer
    offer -- the promotion to be applied
    """
    
    # compares expiration date of offer to current date,
    # purchase count against minimum, and customer premium status
    if offer['exp_date'] < dt.date.today():
        return False
    if customer['purchase_count'] > 2 or customer['premium'] == True:
        return True
    return False

# Question 5
# Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# creates dictionary with values the result of boolean tests of username and password
credential_verification = {'p_length > 5': len(password) > 5, 'u_length < 20': len(username) < 20, 'p != u': password != username}


