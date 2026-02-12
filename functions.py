from game_data import data 
import random

index_list  = [0]

def populate_index():
    new_index = 0
    while len(index_list) < len(data):
        new_index += 1 
        index_list.append(new_index)
    print(index_list)


def select_index(a,b):
    
    print(index_list)
    index_a =  random.choice(index_list)
    print(index_a)
    index_list.remove(index_a)
    print(index_list)
    index_b = random.choice(index_list)
    print(index_b)
    index_list.remove(index_b)
    print(index_list)


