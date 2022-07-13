# Question 1
# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

total_rental_price = (3 + 5 + 1) * 3
print(total_rental_price)


# Question 2
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

gross_pay = (400 * 6) + (380 * 4) + (350 * 10)
print(gross_pay)

# Question 3
# # A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

import datetime
ethics_101 = {'e_cap': 25, 'e_cur': 25, 'weekday': 'Thu', 'start_time': datetime.timedelta(), 'duration': 90}
psyc_101 = {}
math_1 = {} 
eng_1b = {} 
math_13 = {}
student_schedule = (psyc_101, math_1, eng_1b, math_13)

def conflict_check(schedule, section):
    if section['e_cap'] == section['e_cur']:
        return 'Class Full'

    for item in schedule:
        if ethics_101['weekday'] == item['weekday']:
            if 

    return 'Student may join.'

# Question 4
# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

customer_1 = {'purchase_count': 1, 'premium': True}
promotion_1 = {'discount': .85, 'exp_date': datetime.date(2021, 12, 31)}

def apply_offer(customer, offer):
    if offer['exp_date'] < date.today():
        return False
    if customer['purchase_count'] > 2 or customer['premium'] == True:
        return True
    return False

# Question 5
# Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
credential_verification = {'p_length > 5': len(password) > 5, 'u_length < 20': len(username) < 20, 'p != u': password == username}

