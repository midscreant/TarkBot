# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:28:38 2022

@author: vinch
"""

from recipes___ import all_recipes

class InfoGrabber:
    
    def __init__(self):
        self.workbench_recipes_1 = all_recipes["Workbench"][0]
        self.workbench_recipes_2 = all_recipes["Workbench"][1]
        self.workbench_recipes_3 = all_recipes["Workbench"][2]
        self.all_works = [self.workbench_recipes_1, self.workbench_recipes_2, self.workbench_recipes_3] 
    
    def getInfo(self):
        #returns valid dict
        preset_dict = {}
        _exit = False 
        
        i=0
        for work in self.all_works:
            print("\n")
            print("Level " + str(i+1) + " Workbench Crafts")
            print("<><><><><><><><><><><><><><><>")
            for recipe_name in work.keys():
                print(recipe_name)
            i += 1
            
        while _exit == False:
            total_keys = list(self.workbench_recipes_1.keys()) + list(self.workbench_recipes_2.keys()) + list(self.workbench_recipes_3.keys())  
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
                            preset_dict["workbench"] = (key)
                            print(key + " successfully selected")
                            while True:
                                response = input("How many times do you want to run this? (-1 means as many as possible within time):  \n")
                                try:
                                    if type(int(response)) != int:
                                        print("Error: Invalid response")
                                        continue
                                    print("Count of " + response + " accepted." )
                                except ValueError:
                                    print("Error: Invalid response")
                                    continue
                            break
                        elif response.lower() == 'n':
                            z_exit = True 
                        else:
                            print("Invalid response. Type y or n")
                if _exit == True:
                    break
            
        