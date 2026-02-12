from game_data import data 
import random

index_list  = [0]
index_a = 0
index_b = 0 

option_a = {}
option_b = {}

user_choice = ""
remaining_choice = 0
user_guess = 0

def populate_index():
    new_index = 0
    while len(index_list) < len(data):
        new_index += 1 
        index_list.append(new_index)
    return index_list    


def select_index():
    global index_a, index_b
    print(index_list)
    index_a = random.choice(index_list)
    print(index_a)
    index_list.remove(index_a)
    print(index_list)
    index_b = random.choice(index_list)
    print(index_b)
    index_list.remove(index_b)
    print(index_list)


def present_options():
    global option_a, option_b
    option_a = data[index_a]
    option_b  = data[index_b]
    print(f"Choose between option A: {option_a['name']}, a {option_a['description']} from {option_a['country']}")
    print(f"Or option B : {option_b['name']}, a {option_b['description']} from {option_b['country']}")


def user_choice():
    global remaining_choice, user_guess
    followers_a =  option_a['follower_count']
    followers_b =  option_b['follower_count']
    user_choice = input("type A or B: ").capitalize()
    if user_choice == 'A' :
        user_guess = followers_a
        print("outcome #1")
        remaining_choice = followers_b
    elif user_choice == 'B' :
        user_guess = followers_b
        print("outcome #2")
        remaining_choice = followers_a
    
    print(user_guess,remaining_choice)
    