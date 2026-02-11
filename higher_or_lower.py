from game_data import data 
import random

# compare game should 
# 1) print the first contender in and f string such that 
# Compare A : 'name' , a 'description' , from 'country'
# Present the comparasion with a similar line 
# compare the value of followers 

#potentially make two fucntion, one to present the game and one two actuallly compare

print("welcome to higher or lower")

indexes  = [0]
new_index = 0
for item in data - 1 :
    new_index += 1
    indexes.append(new_index)

print(indexes)

option_a = data[random.randint(0,len(data)-1)]
option_b  = data[random.randint(0,len(data)-1)]

print(f"Choose between option A: {option_a['name']}, a {option_a['description']} from {option_a['country']}")
print(f"Or option B : {option_b['name']}, a {option_b['description']} from {option_b['country']}")




def user_choice():
   
    followers_a =  option_a['follower_count']
    followers_b =  option_b['follower_count']
    user_choice = input("type A or B: ").capitalize()
    if user_choice == 'A' :
        user_guess = followers_a
        # remaining_choice = followers_b
    elif user_choice == 'B' :
        user_guess = followers_b
        # remaining_choice = followers_a
    return user_guess




# def copare(option_A,Option_B):
