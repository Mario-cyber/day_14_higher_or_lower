from game_data import data 
import random

# compare game should 
# 1) print the first contender in and f string such that 
# Compare A : 'name' , a 'description' , from 'country'
# Present the comparasion with a similar line 
# compare the value of followers 

#potentially make two fucntion, one to present the game and one two actuallly compare


option_a = data[random.randint(0,len(data)-1)]['name']
option_b  = data[random.randint(0,len(data)-1)]['name']

print(option_a)
print(option_b)

