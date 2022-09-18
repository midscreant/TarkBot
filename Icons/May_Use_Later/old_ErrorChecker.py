# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:44:46 2022

@author: vinch
"""

from Hideout import Hideout
from inspect import getmembers, isfunction

class ErrorChecker:
    
    #put try excepts in executor class
    
    def __init__(self, root_path):
        
        self.funct_list = getmembers(Hideout, isfunction)
        self.the_hideout = Hideout(root_path)
        
    def errorChecker(self, funct_name, iterator=0, *arguments):
        #values in argument list must be structured in order or it will fail 
        #MUST CREATE HIDEOUT OBJECT TO WORK
        #may need to pass in arguments for function too 
        
        print(iterator)
        
        if iterator == 3:
            print(funct_name+" failed after 3 attempts...")
            return "MEGAFAIL" 
            
        for name, value in self.funct_list:
            if funct_name.lower() == str(name).lower():
                print("Name and funct found!")
                status = None
                if len(arguments) > 0:
                    new_args = arguments[0]
                    if type(arguments) == tuple and type(new_args) != tuple:
                        status = value(self.the_hideout, arguments)
                    while True:
                        if type(new_args[0]) == tuple: 
                    #WILL FAIL FOR FUNCTIONS THAT TAKE TUPLES AS ARGS
                            new_args = new_args[0]
                            continue
                        else:
                            status = value(self.the_hideout, new_args) 
                            break
                else:
                    status = value(self.the_hideout)
                if status == "fail": 
                    status_2 = self.errorChecker(funct_name, iterator+1, arguments)
                    if status_2 == "MEGAFAIL":
                        return "MEGAFAIL"
                    else:
                        print("funct ran successfully on try")
                        return "pass"
                else:
                    print(funct_name+" ran successfully")
                    return "pass"        
                ##maybe name()
                ##maybe value()
                ##maybe exec(value) 
        print("No funct found...error checker failed :(  ") 
        return "MEGAFAIL"

# my_checker = ErrorChecker()
# print(my_checker.errorChecker( "startRecipe",0,"MOON", "scav"))  
# print(my_checker.errorChecker("hideoutMoveLeft", 0))
       