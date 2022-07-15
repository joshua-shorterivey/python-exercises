from function_exercises import calculate_tip
import itertools
print(itertools.combinations('abcd', 2))

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3? 9
combine_letters = list(iter.product('abc', '123'))
len(combine_letters)

#How many different combinations are there of 2 letters from "abcd"? 6
different = len(list(iter.combinations('abcd', 2)))

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
combine_letters = list(iter.product('abc', '123'))
len(combine_letters)

#How many different combinations are there of 2 letters from "abcd"? 6
different = len(list(iter.combinations('abcd', 2)))
different

# How many different permutations are there of 2 letters from "abcd"? 12
diff_perm = list(iter.permutations('abcd', 2))
len(diff_perm)

# Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
# Use the load function from the json module to open this file.
import json
profiles = json.load(open('profiles.json'))

#Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

# Total number of users -- 19
len(profiles)
# Number of active users -- 9
len([user for user in profiles if user['isActive'] == True])

# Number of inactive users -- 10
len([user for user in profiles if user['isActive'] != True])

# Grand total of balances for all users -- $52,667.02
balance_list = [float(user['balance'].replace('$', '').replace(',' , '')) for user in profiles]
sum(balance_list)

# Average balance per user -- $2,771.95
round(sum(balance_list) / len(balance_list), 2)

# User with the lowest balance -- Avery Flynn
for user in profiles:
    if float(user['balance'].replace('$', '').replace(',' , '')) == min(balance_list):
        print(user['name'])
        
# User with the highest balance -- Fay Hammond
for user in profiles:
    if float(user['balance'].replace('$', '').replace(',' , '')) == max(balance_list):
        print(user['name'])
        
# Most common favorite fruit -- Strawberry: 9
# Least most common favorite fruit -- apple: 4

fruits_dict = {}
for user in profiles:
    fruit = user['favoriteFruit']
    if f'{fruit}' not in fruits_dict:
        fruits_dict[f'{fruit}'] = 1
    else: 
        fruits_dict[f'{fruit}'] += 1
    print(fruits_dict)
    
sorted(fruits_dict.items(), key=lambda x:x[1])

# Total number of unread messages for all users -- 210
total_unread = 0
unread = '' #immutable place holder for eventual join
for user in profiles:
    unread_count = [char for char in user['greeting'] if char.isnumeric()]
    total_unread += int(unread.join(unread_count))

        
        
        
        
        