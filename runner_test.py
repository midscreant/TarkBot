# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:57:43 2022

@author: vinch
"""

#RUNNER

from recipes___ import all_recipes
from Hideout import Hideout
from time import sleep

#<><><><><><><><><><><><><><><><><><><>
#Initial user input grab
#<><><><><><><><><><><><><><><><><><><>

workbench_recipes_1 = all_recipes["Workbench"][0]
workbench_recipes_2 = all_recipes["Workbench"][1]
workbench_recipes_3 = all_recipes["Workbench"][2]

all_works = [workbench_recipes_1, workbench_recipes_2, workbench_recipes_3]
i = 0    
for work in all_works:
    print("\n")
    print("Level " + str(i+1) + " Workbench Crafts")
    print("<><><><><><><><><><><><><><><>")
    for recipe_name in work.keys():
        print(recipe_name)
    i += 1    


_exit = False 
_item_name = ""


while _exit == False:
    total_keys = list(workbench_recipes_1.keys()) + list(workbench_recipes_2.keys()) + list(workbench_recipes_3.keys())  
    item_name = input("\n\nPlease enter item name (or keyword from it. Length > 5):\n<><><>\n")
    if len(item_name) < 6:
        print("Error: String must be 6+ digits ")
        continue
    for key in total_keys: 
        if item_name.lower() in key.lower(): 
            z_exit = False
            while z_exit == False: 
                response = input("Did you mean, " + key + "? (y/n)\n")
                if response.lower() == 'y':
                    _exit = True
                    z_exit = True
                    _item_name = key
                    print(key + " successfully selected")
                    break
                elif response.lower() == 'n':
                    z_exit = True 
                else:
                    print("Invalid response. Type y or n")
        if _exit == True:
            break 

#<><><><><><><><><><><><><><><><><><><>
#Hideout Creation and Execution
#<><><><><><><><><><><><><><><><><><><>

my_hideout = Hideout()

_exit = False
while _exit == False:
    prompt = input("Ready to begin? 5 Sec clock starts after input. (y/n):\n<><><>\n")
    if prompt.lower() == 'y':
        _exit = True
        sleep(5)

my_hideout.goToHideout()
my_hideout.makeRecipe(_item_name)
        
                 
    