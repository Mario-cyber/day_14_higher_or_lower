from game_data import data 

import functions as fn 


fn.populate_index()

print(fn.populate_index())

fn.select_index()

fn.present_options()

fn.user_choice()

fn.comparison()


''' Need to finish up functionality that makes chosen option, default option if corret.
alternatively, intead of messing around with indexes, you could make a local object to hold the infromation 
you need and swap it out as needed '''