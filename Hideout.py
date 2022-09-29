# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:58:08 2022

@author: vinch
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:22:17 2022

@author: vinch
""" 
#Hideout v2

#<><><><><><><><>
#---------------
#TarkovBotV2
#---------------
#<><><><><><><><>
 
import pyautogui as pygui
from time import sleep 
import cv2
import os 
from recipes___ import all_recipes

#CURRENT DEPENDENCIES
    #pyautogui, cv2
 
class Hideout:
    
    def __init__(self, base_path):

        self.base_path = base_path
        #icons path
        self.icons_path = os.path.join(self.base_path, 'Icons')
        #nodes path
        self.nodes_path = os.path.join(self.icons_path, 'Nodes') 
        #submenu options path
        self.submenu_path = os.path.join(self.icons_path, "Submenu_Options")
        #recipes path
        self.recipes_path = os.path.join(self.icons_path, "Recipes")
        #workbench recipes path
        self.workbench_recipes_path = os.path.join(self.recipes_path, "Workbench")
        #nutrition recipes path
        self.nutrition_recipes_path = os.path.join(self.recipes_path, "Nutrition")
        #intel recipes path
        self.intel_recipes_path = os.path.join(self.recipes_path, "Intel")
        #medstation recipes path
        self.medstation_recipes_path = os.path.join(self.recipes_path, "Medstation")
        #scav recipes path
        self.scav_recipes_path = os.path.join(self.recipes_path, "Scav")
        #lavatory recipes path
        self.lavatory_recipes_path = os.path.join(self.recipes_path, "Lavatory")
 
        #initial hideout press
        self.initial = False
        
        #lists of dicts
            #dicts are recipe books {recipe_name:{ingredient_1:count, ...}} 
        self.workbench_recipes = all_recipes["Workbench"]
        self.nutrition_recipes = all_recipes["Nutrition"]
        self.intel_recipes = all_recipes["Intel"]
        self.medstation_recipes = all_recipes["Medstation"]
        self.lavatory_recipes = all_recipes["Lavatory"]
        
        #complete dicts
        self.full_workbench_recipes = self.workbench_recipes[0] | self.workbench_recipes[1] | self.workbench_recipes[2] 
        self.full_nutrition_recipes = self.nutrition_recipes[0] | self.nutrition_recipes[1] | self.nutrition_recipes[2]
        self.full_intel_recipes = self.intel_recipes[0] | self.intel_recipes[1] 
        self.full_medstation_recipes = self.medstation_recipes[0] | self.medstation_recipes[1] | self.medstation_recipes[2]
        self.full_lavatory_recipes = self.lavatory_recipes[0] | self.lavatory_recipes[1] | self.lavatory_recipes[2]
        
        #name dicts
        self.workbench_names = all_recipes["Workbench - Names"]
        self.nutrition_names = all_recipes["Nutrition - Names"]
        self.intel_names = all_recipes["Intel - Names"]
        self.medstation_names = all_recipes["Medstation - Names"]
        self.scav_names = all_recipes["Scav - Names"]
        self.lavatory_names = all_recipes["Lavatory - Names"]
        
    #<><><><><><><><><><><><><>
    #Simple Hideout Functions 
    #<><><><><><><><><><><><><>
    
    def goToHideout(self):
        #Click "Hideout" (Bottom)
        pygui.click(x=201, y=1057)
        if self.initial == False: 
            self.initial = True
            sleep(10)
        sleep(1.75)    
 
    
    def hideoutReset(self): 
        #reset to middle
        pygui.press('enter')
        sleep(1) 
        pygui.press('esc')
        sleep(1.5)
         
        
    def hideoutMoveLeft(self): 
        self.hideoutReset()
        #Move left 
        pygui.moveTo(x=1,y=540)
        sleep(0.325)
        pygui.moveTo(x=960,y=540)
        sleep(0.5)
        
        
    def hideoutMoveRight(self):
        self.hideoutReset()
        #Move right
        pygui.moveTo(x=1919,y=540)
        sleep(0.45)
        pygui.moveTo(x=960,y=540) 
        sleep(0.5)
        
    def goToMainMenu(self):
        #ADD CHECK FOR CONFIRMATION PROMPT AS THIS WONT WORK WHEN THOSE APPEAR
        sleep(1)
        pygui.click(x=0, y=500)
        sleep(0.2)
        pygui.press('esc')
        sleep(0.2)
        pygui.press('esc')
        sleep(0.2)
        pygui.press('esc')
        sleep(0.2)
        pygui.press('esc')
        sleep(0.2)
        pygui.press('esc')
        sleep(0.5)
        #CONFIRMATION
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("MainMenu_block.png", confidence=0.9) == None:
            #MEANS YOU ARE NOT ON MAIN MENU SCREEN
            print("FATAL ERROR: Not on home screen...")
            return "FATAL"
        print("On main menu")
        sleep(0.3)
        
        
    #<><><><><><><><><><><><><>    
    #Passive Hideout Functions
    #<><><><><><><><><><><><><>
    
    def checkForClaim(self, node_name):
        os.chdir(self.submenu_path)
        #extension is _claim
        dir_list = [f for f in os.listdir('.') if os.path.isfile(f) and '_claim' in f]
        for claim in dir_list:
            if pygui.locateCenterOnScreen(claim, confidence=0.75) != None:
                if node_name != "scav":
                    point_x, point_y = pygui.locateCenterOnScreen(claim,confidence=0.75)
                    pygui.click(x=point_x, y=point_y)
                    print("Item claimed")
                    return
                point_x, point_y = pygui.locateCenterOnScreen(claim,confidence=0.75)
                pygui.click(x=point_x, y=point_y)
                print("Item claimed")
                sleep(1)
                _point_x, _point_y = pygui.loacteCenterOnScreen("receive_claim.png", confidence=0.75)
                pygui.click(x=_point_x, y=_point_y)
                print("And received")
                return
            else:
                continue
        return 'none'
    
    def getAllItems(self):
        #need to somehow stop if hideout doesnt have all nodes
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        
        self.goToHideout()
        
        os.chdir(self.nodes_path)
        dir_list = [f for f in os.listdir('.') if os.path.isfile(f) and '_node' in f]
        _clicked = False
        for node in dir_list:
            if pygui.locateOnScreen(node, confidence=0.9) != None:
                point_x, point_y = pygui.locateCenterOnScreen(node, confidence=0.8)
                pygui.click(x=point_x, y=point_y)
                sleep(0.5)
                _clicked = True
                break
        if _clicked == False:
            print("Error. No node found")
            return "fail"
        
        scroll_nodes = ["medstation", "lavatory", "scav", "intel", "workbench", "nutrition"]
                    
        claimed_count = 0
        os.chdir(self.submenu_path)
        for i in range(20):
            complete = False
            for node in scroll_nodes:
                node_name = node + "_name.png"
                if pygui.locateOnScreen(node_name, confidence=0.75) != None:
                    _exit_count = 0
                    if node == "medstation":
                        _exit_count = 50
                    elif node == "scav":
                        _exit_count = 15
                    elif node == "intel":
                        _exit_count = 35
                    elif node == "workbench":
                        _exit_count = 150
                    elif node == "nutrition":
                        _exit_count = 42
                    elif node == "lavatory":
                        _exit_count = 100
                    _i = 0
                    if _exit_count > 0:
                        while True:
                            if _i >= _exit_count:
                                complete = True
                                break
                            pygui.moveTo(x=1410, y=655)
                            pygui.scroll(-10)
                            _i += 1
                            status = self.checkForClaim(node)
                            if status == None:
                                print("Claimed 2")
                                claimed_count += 1
                                print('Done Scrolling')
                                complete = True
                                break
            if complete == False:
                    status = self.checkForClaim("na")
                    if status == None:
                        print("Claimed")
                        claimed_count += 1
            sleep(0.5)
            pygui.click(x=1870, y=999)
            sleep(0.5)
            
        print("Successfully grabbed " + str(claimed_count) + " item(s)")
        
        
        
        
    
 
    #<><><><><><><><><><><><><>
    #Active Hideout Functions
    #<><><><><><><><><><><><><>

    def bottomFlea(self):
        pygui.click(x=1228, y=1066)
        sleep(1)
    
    def startRecipe(self, item_pic_name, node_name=None):
        print(item_pic_name)
        if type(item_pic_name) == tuple:
            if node_name != None:
                print("Error. Both tuple and node name")
                return 'fail' 
            item_pic_name_list = item_pic_name
            print(item_pic_name_list)
            item_pic_name = item_pic_name_list[0] 
            node_name = item_pic_name_list[1] 
        if node_name.lower() == "med": 
            os.chdir(self.medstation_recipes_path)
        elif node_name.lower() == "intel": 
            os.chdir(self.intel_recipes_path)
        elif node_name.lower() == "nutrition": 
            os.chdir(self.nutrition_recipes_path)
        elif node_name.lower() == "workbench": 
            os.chdir(self.workbench_recipes_path)
        elif node_name.lower() == "scav": 
            os.chdir(self.scav_recipes_path)
        elif node_name.lower() == "lav":
            os.chdir(self.lavatory_recipes_path)
        else:
            print("Error: Invalid node name...")
            return 'fail' 
        item_loc = pygui.locateOnScreen(item_pic_name + "_recipe.png", confidence=0.925) 
        if item_loc != None:
            item_left_x = item_loc.left
            item_width = item_loc.width 
            item_x, item_y = pygui.center(item_loc) 
            #shift 72 pixels right to click start button
            pygui.click(x=item_left_x + item_width + 72, y=item_y)
            sleep(0.25)
            pygui.press("y")
            #Should add a confirmation check here
            sleep(2)
            os.chdir(self.submenu_path)
            if pygui.locateOnScreen("production_status.png", confidence=0.9) != None:
                print("Recipe for " + item_pic_name + " successfully started") 
            #successful start
                return
            else:
                print("Error 0003: No " + item_pic_name + " start found. Maybe a misclick") 
                return "fail" 
        else:
            print("Error 0003: No " + item_pic_name + " start found") 
            return "fail" 
    
    
    def buyAid(self, count=None, offset=None):
        #assumes you are on flea and at correct item, as does parent  
        #FIRST PURCHASE POINT (x=1761, y=179)
        #offset is an int for jumping down a certain count
        if count != None: 
            if offset == None or offset == 0:
                pygui.click(x=1761, y=179)
                sleep(0.5)
                pygui.doubleClick(x=1035, y=490)
                sleep(0.25)
                pygui.write(str(count), interval=0.075)
                sleep(0.25)
                pygui.press("y")
                sleep(0.75)
            else:    
                pixel_offset = 72 * offset
                pygui.click(x=1762, y=179+pixel_offset)
                sleep(0.5)
                pygui.doubleClick(x=1035, y=490)
                sleep(0.25)
                pygui.write(str(count), interval=0.075)
                sleep(0.25)
                pygui.press("y")
                sleep(0.75) 
        elif offset == None or offset == 0:
            pygui.click(x=1761, y=179)
            sleep(0.25)
            pygui.press("y")
            sleep(0.75)
        else:
            pixel_offset = 72 * offset
            pygui.click(x=1762, y=179+pixel_offset)
            sleep(0.25)
            pygui.press("y")
            sleep(0.75)
       
        
    def buyOnFlea(self, count, item_name, offset=None):  
        _index = 0
        _z = 0 
        _exit = 0 
        if count > 5 and count <= 10:
            #does extra attempts for more items
            _exit = 12
        else:
            _exit = 8 
        os.chdir(self.submenu_path)
        while _index < count and _z < _exit: 
            if _z % 3 == 0:
                if pygui.locateCenterOnScreen("FleaRefresh_button.png",confidence=0.9) != None:
                    point_x, point_y = pygui.locateCenterOnScreen("FleaRefresh_button.png",confidence=0.9)
                    pygui.click(x=point_x, y=point_y)
                else:
                    print("ERROR: No refresh button found")
            if count > 3:
                #moves to stack purchase
                self.buyAid(count, offset)
            else:
                self.buyAid(offset=offset) 
            if pygui.locateOnScreen("PurchaseComplete_option.png", confidence=0.7) != None:
                _index += 1
                if count > 3:
                    print("Stack of "+str(count)+" "+item_name+"s successfully purchased...")
                    return
                sleep(2.25)
            else:
                print("Purchase failed, retrying")
                _z += 1
        if _z == _exit:
            if _index == 0: 
                print("All purchases failed")
            else:
                end_count = count - _index
                print(str(_index) + " successful purchases. " + str(end_count) + " failed.")
            sleep(0.25)
            return "fail"
        else:
            sleep(0.25)
            print("All "  + str(count) + " " + item_name + "(s) bought")       
 
    
    def fleaMarketSearch(self, item_name):
        #assumes you are already on the flea
        #assumes you already have a specific item selected 
        #click text box 
        pygui.click(x=258, y=121)
        pygui.write(item_name, interval=0.2525)
        sleep(0.3)
        pygui.press('enter')
        sleep(0.35)
        #supposed to click Xs
        os.chdir(self.submenu_path)
        all_points = list(pygui.locateAllOnScreen("Exit_Option.png", confidence=0.9))
        if len(all_points) == 3: 
            point_1x, point_1y  = pygui.center(all_points[0]) 
            pygui.click(x=point_1x, y=point_1y)
            sleep(0.3)
            refreshed_points = list(pygui.locateAllOnScreen("Exit_Option.png", confidence=0.9))
            point_2x, point_2y = pygui.center(refreshed_points[1]) 
            pygui.click(x=point_2x, y=point_2y)
            sleep(1)
        #clicks item name on left
        if item_name.lower() == 'pliers' or item_name.lower() == 'screwdriver':
            #these items were problomatic so added extra check. position 3
            pygui.click(x=155, y=234)
        elif 'm856' in item_name.lower() or 'm855' in item_name.lower():
            #these too. position 2
            pygui.click(x=218, y=196)
        else:    
            pygui.click(x=187, y=164)
        sleep(1)
        
        
    def checkAndBuyRecipe(self, recipe):
        #EXPECTS YOU TO HAVE ALREADY MOVED TO IT ON SCREEN
        #THIS IS THE BRUTE FORCE BUY. DOES NO CHECKS FOR CURRENT ITEM COUNT    
        #recipe {"ingredient_1":count, ...} 
        print("<><><><><><><><><><>")
        print("Shopping list ready")
        print("---------------------")
        print(recipe)
        print("<><><><><><><><><><>") 
        self.bottomFlea()
        sleep(1)
        if type(recipe) != dict:
            #this means scav
            self.fleaMarketSearch(recipe)
            self.buyOnFlea(1, recipe)
            return
        for name, count in list(recipe.items()):
            _name = name
            if name.endswith("-_-"):
                _name = name[:-3]
            
            self.fleaMarketSearch(_name)
            self.buyOnFlea(count, _name)        
            sleep(1)    
     
        
    def reusableExitLoop(self, item_name, node_name):
        #item name is a string to a .png
        #img should be of item + count and a side recipe item to confirm its at the right one
        #NEED TO TEST SCROLL COUNT
        _exit = False
        _i = 0
        recipe_tuple, recipe_pic_name = self.findRecipe(item_name, node_name)
        _exit_count = 0
        if node_name == "med":
            _exit_count = 50
            os.chdir(self.medstation_recipes_path)
        elif node_name == "intel":
            _exit_count = 35
            os.chdir(self.intel_recipes_path)
        elif node_name == "nutrition":
            _exit_count = 42
            os.chdir(self.nutrition_recipes_path)
        elif node_name == "workbench":
            _exit_count = 150
            os.chdir(self.workbench_recipes_path)
        elif node_name == "scav":
            _exit_count = 15
            os.chdir(self.scav_recipes_path)
        elif node_name == "lav":
            _exit_count = 100
            os.chdir(self.lavatory_recipes_path)
        else:
            print("Error: Invalid node name passed")
            return 'fail'
        while _exit == False: 
            if pygui.locateOnScreen(recipe_pic_name + "_recipe.png", confidence=0.9) != None: 
                _exit = True
            if _i > _exit_count:
                print("No item found after " + str(_exit_count) + " attempts")
                return 'fail'
            _i += 1
            pygui.moveTo(x=1410, y=655) 
            pygui.scroll(-10)
 
    
    def locateNode(self, node_name):
        if type(node_name) == tuple:
            node_name = str(node_name[0])
        self.goToHideout()
        #add
        #node names - "med", "nutrition", "workbench", "intel"
            #right left node list
        right_nodes = ["heating", "library", "rest", "med", "nutrition", "booze", "water"]
        left_nodes = ["workbench", "intel", "lav", "btc"]
        middle_nodes = ["generator", "scav"]
        os.chdir(self.nodes_path)
        file_list = [f for f in os.listdir('.') if os.path.isfile(f) and node_name in f.lower()]
        if node_name in right_nodes:
            self.hideoutMoveRight()
        elif node_name in left_nodes:
            self.hideoutMoveLeft()
        else:
            print("No movement needed")
        for file in file_list:
            if pygui.locateOnScreen(file, confidence=0.7) != None:
                node_x, node_y = pygui.locateCenterOnScreen(file, confidence=0.7)
                pygui.click(x=node_x, y=node_y)
                print(node_name + " found and clicked...")
                sleep(1)
                return True
        print("No node found. Could not click")
        return "fail"
    
    
    def findRecipe(self, recipe_name, node_name):
        #returns tuple (recipe_dict, recipe_pic_name)
        recipe_pic_name = " "
        dir_1 = " "
        dir_2 = " "
        if node_name == "workbench":
            dir_1 = self.workbench_names
            dir_2 = self.full_workbench_recipes
        elif node_name == "nutrition":
            dir_1 = self.nutrition_names
            dir_2 = self.full_nutrition_recipes 
        elif node_name == "intel":
            dir_1 = self.intel_names
            dir_2 = self.full_intel_recipes 
        elif node_name == "med":
            dir_1 = self.medstation_names
            dir_2 = self.full_medstation_recipes 
        elif node_name == "lav":
            dir_1 = self.lavatory_names
            dir_2 = self.full_lavatory_recipes
        elif node_name == "scav":
            dir_1 = {}
            for name, value in list(self.scav_names.items()):
                if value == recipe_name:
                    return (value, name)
            
        for name, value in list(dir_1.items()): 
            if name == recipe_name:
                recipe_pic_name = value
                break
        if recipe_pic_name == " ":
            print("Error: No recipe pic name grabbed") 
            return 'fail'
        for name, value in list(dir_2.items()):
            if name == recipe_name: 
                return ((name, value), recipe_pic_name)
        print("Error: No recipe for " + recipe_name + " found") 
        return 'fail'
        
   
    def makeRecipe(self, recipe_name):
        #separate scav funct
        node_name = ""
        final_recipe_name = recipe_name
        while True:
            if type(final_recipe_name) == str:
                break
            if type(final_recipe_name) == None:
                print("Error: None type not valid recipe")
                return 'fail'
            if type(recipe_name) == tuple and final_recipe_name == None:
                final_recipe_name == recipe_name[0]
                continue
            elif type(final_recipe_name) == tuple:
                final_recipe_name == final_recipe_name[0]
                continue
            elif type(final_recipe_name[0]) == str:
                final_recipe_name = final_recipe_name[0]
                break
            else:
                print("Error: No recipe name found after tuple dive")
                return 'fail'
        if final_recipe_name in list(self.full_workbench_recipes.keys()):
            node_name = "workbench"
        elif final_recipe_name in list(self.full_nutrition_recipes.keys()):
            node_name = "nutrition"
        elif final_recipe_name in list(self.full_intel_recipes.keys()):
            node_name = "intel"
        elif final_recipe_name in list(self.full_medstation_recipes.keys()):
            node_name = "med"
        elif final_recipe_name in list(self.scav_names.values()):
            node_name = "scav"
        elif final_recipe_name in list(self.full_lavatory_recipes.keys()):
            node_name = "lav"
        else:
            print(final_recipe_name)
            print("Error: Invalid recipe")
            pygui.press("esc")
            return 'fail'
 
        #basic testing complete
        #need to test confidence levels
        #error checking is next big step
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        # node_located = self.locateNode(node_name) 
        # if node_located == True:   
            # sleep(1) 
            # self.reusableExitLoop(recipe_name, node_name)
        if node_name == "scav":
            scav_recipe_name, scav_pic_name = self.findRecipe(recipe_name, node_name)
            if scav_pic_name != "25" and scav_pic_name != "150" and scav_pic_name != "950":
                self.checkAndBuyRecipe(scav_recipe_name)
            self.goToHideout()
            _node_located = self.locateNode(node_name)
            if _node_located == True:
                self.reusableExitLoop(scav_recipe_name, node_name)
                self.startRecipe(scav_pic_name, node_name)
                pygui.press("esc")
            else:
                print("Error 0002: No node found. Exiting... ")
                pygui.press("esc")
                return "fail" 
        else:
            recipe_tuple, recipe_pic_name = self.findRecipe(recipe_name, node_name)
            _recipe_name, recipe_value = recipe_tuple 
            self.checkAndBuyRecipe(recipe_value)  
            self.goToHideout()
            _node_located = self.locateNode(node_name)
            if _node_located == True:
                self.reusableExitLoop(recipe_name, node_name)
                self.startRecipe(recipe_pic_name, node_name)
                pygui.press("esc")
            else:
                print("Error 0002: No node found. Exiting... 1 ")
                pygui.press("esc")
                return "fail"
            
        
        
    
        ###EVERYTHING BELOW HERE UNTESTED AS OF 9/8/22
    
    def goToTraders(self):
        #assumes you can see button
        #clicks bottom traders button
        pygui.click(x=1112, y=1053)
        sleep(1)
        
        
    def goToJaeger(self):
        #assumes you are on traders screen
        pygui.click(x=1227, y=664)
        sleep(1)
        
        
    def clickMidLeft(self, pic_name):
        first_loc = pygui.locateOnScreen(pic_name, confidence=0.95)
        #moving to mid left of button
        _left, _top, _width, _height = first_loc
        _height = _height/2
        _width = _width - 5
        point_x = _left + _width
        point_y = _top + _height
        pygui.click(x=point_x, y=point_y)
        sleep(0.25)
        
        
    def quickOrganizeInv(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        #click bottom character
        pygui.click(x=960, y=1064)
        sleep(0.25)
        #click auto-sort and confirm
        pygui.click(x=1244, y=922)
        sleep(0.25) 
        pygui.press('y')  
        sleep(0.25)
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("sortFail_status.png",confidence=0.9) != None:
            print("Failed to sort stash")
            return "fail"
        else:
            print("Inventory successfully sorted")
 
           
      
    def boozeChecker(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        #NEEDS STATUS PICS 
        self.locateNode('booze')
        os.chdir(self.submenu_path) 
        if pygui.locateOnScreen("production_status.png", confidence=0.9) != None:
            print("Booze currently being produced...")
            pygui.press("esc")
            return
        #Need 5 pics: 0/1, 1/1, 0/2, 1/2, 2/2
        #if 0/1, buy water
        #if 0/2 buy 2 sugar
        #if 1/2 buy 1 sugar
        #start when set 
        superwater_count = 0
        if pygui.locateOnScreen("0-1Status.png", confidence=0.9) != None:
            superwater_count = 1  
        sugar_count = 0
        if pygui.locateOnScreen("0-2Status.png", confidence=0.9) != None:
            sugar_count = 2
        elif pygui.locateOnScreen("1-2Status.png", confidence=0.9) != None:    
            sugar_count = 1 
        if superwater_count > 0:
            self.bottomFlea()
            self.fleaMarketSearch("Canister with purified water")
            self.buyOnFlea(1, "Canister with purified water")
            sleep(0.25)           
        if sugar_count > 0:
            self.goToHideout()
            self.bottomFlea()
            self.fleaMarketSearch("Pack of sugar")
            self.buyOnFlea(sugar_count, "Pack of sugar", 3)
            sleep(0.25)  
        self.locateNode('booze') 
        if pygui.locateOnScreen("StartStatus.png", confidence=0.9) == None:
            print("Error 0009: No start found")
            pygui.press("esc")
            return "fail"
        start_x, start_y = pygui.locateCenterOnScreen("StartStatus.png", confidence=0.9)
        pygui.click(x=start_x, y=start_y)
        sleep(0.25)
        pygui.press('y')
        print('Successfully began moonshine production...') 
        sleep(0.25)
        pygui.press("esc")
    
    
    def btcChecker(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        #deals with btc not graphics
        self.locateNode('btc')
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("GetItemsStatus.png", confidence=0.9) != None:
            status_x, status_y = pygui.locateOnScreen("GetItemsStatus.png", confidence=0.9)
            pygui.click(x=status_x, y=status_y)
            print("Bitcoins claimed...")
            pygui.press("esc")
            return
        print('No bitcoins to be claimed...')
        pygui.press("esc")
        

    def generatorChecker(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        #Checks if generator has room for more fuel, adds or buys and adds if needed
        #generator images in submenu, _gene
        self.locateNode('generator')
        os.chdir(self.submenu_path) 
        
        #sub-process to check for empty fuel containers
        removed_count = 0
        while True:
            if pygui.locateOnScreen("SmallNoFuel_gene.png", confidence=0.925) != None:
                self.clickMidLeft("SmallNoFuel_gene.png")
                point_x, point_y = pygui.locateCenterOnScreen("none_gene.png", confidence=0.9)
                pygui.click(x=point_x, y=point_y)
                sleep(0.5)
                if pygui.locateCenterOnScreen("none_gene.png", confidence=0.9) != None:
                    print("Error. Didn't remove fuel")
                    continue
                print("Empty small fuel removed")
                removed_count += 1
            elif pygui.locateOnScreen("BigNoFuel_gene.png", confidence=0.925) != None:
                self.clickMidLeft("BigNoFuel_gene.png")
                point_x, point_y = pygui.locateCenterOnScreen("none_gene.png", confidence=0.9)
                pygui.click(x=point_x, y=point_y)
                sleep(0.5)
                if pygui.locateCenterOnScreen("none_gene.png", confidence=0.9) != None:
                    print("Error. Didn't remove fuel")
                    continue
                print("Empty big fuel removed")
                removed_count += 1
            else:
                break
            
        print("All empties emptied")
        
        #click traders button
        
        if removed_count > 0:
            self.goToTraders()
            self.goToJaeger()
            pygui.moveTo(x=1621, y=587)
            sleep(0.25)
            scroll_count = 0
            for i in range(removed_count):
                while True:
                    pygui.scroll(-10)
                    scroll_count += 1
                    if scroll_count > 125:
                        print("wasn't able to find all of the fuel")
                        return "FATAL"
                    if pygui.locateOnScreen("SmallFuelEmptySale_gene.png", confidence=0.925) != None:
                        point_x, point_y =  pygui.locateCenterOnScreen("SmallFuelEmptySale_gene.png", confidence=0.925)
                        with pygui.hold("ctrl"):
                            pygui.click(x=point_x, y=point_y)
                        break
                    elif pygui.locateOnScreen("BigFuelEmptySale_gene.png", confidence=0.925) != None:
                        point_x, point_y =  pygui.locateCenterOnScreen("BigFuelEmptySale_gene.png", confidence=0.925)
                        with pygui.hold("ctrl"):
                            pygui.click(x=point_x, y=point_y)
                        break
            point_x, point_y = pygui.locateCenterOnScreen("deal_claim.png", confidence=0.925)
            pygui.click(point_x, point_y)
            if self.goToMainMenu() == "FATAL":
                return "FATAL"
            self.goToHideout() 
            self.locateNode('generator')
            self.clickMidLeft("NoFuel_gene.png")
                
        if pygui.locateOnScreen("BigFuelLoader_gene.png", confidence=0.9) != None:
            fuel_loc_x, fuel_loc_y = pygui.locateCenterOnScreen("BigFuelFull_gene.png")
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Large Fuel Loaded")
            pygui.press("esc") 
            return
        elif pygui.locateOnScreen("SmallFuelLoader_gene.png", confidence=0.9) != None:
            fuel_loc_x, fuel_loc_y = pygui.locateCenterOnScreen("SmallFuelFull_gene.png")
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Small Fuel Loaded") 
            pygui.press("esc")
            return
        else:
            self.fleaMarketSearch("Metal Fuel Tank") 
            fuel_loc = pygui.locateOnScreen("JaegerFuelPrice_gene.png", confidence=0.9)
            fuel_point_x, fuel_point_y = pygui.center(fuel_loc)
            fuel_left_x = fuel_loc.left 
            purchase_loc_x = fuel_left_x + fuel_loc.width + 275
            pygui.click(x=purchase_loc_x, y=fuel_point_y)
            sleep(0.25)
            pygui.press('y') 
            print("Large Fuel Successfully Purchased")
            #can fail if sold out or not enough $. Add check
            sleep(1)
            self.locateNode('generator')
            self.clickMidLeft("NoFuel_gene.png")
            fuel_loc_x, fuel_loc_y = pygui.locateOnScreen("BigFuelFull_gene.png", confidence=0.9)
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Large Fuel Loaded")
            pygui.press("esc")
            return     
        
    
    def waterChecker(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        #all checkers auto load and buy if empty 
        self.locateNode('water')
        os.chdir(self.submenu_path)
        #if there's already a filter loaded, function ends
        if pygui.locateOnScreen("NoFuel_gene.png", confidence=0.9) == None:
            print("Water filter currently loaded and running...")
            pygui.press("esc")
            return
        self.clickMidLeft()
        #if there's no water filters ready to be loaded, buy one on market
        if pygui.locateOnScreen("NoFuelLoader_gene.png", confidence=0.9) != None:
            print("No spare water filters. Buying one from market...")
            self.bottomFlea()
            self.fleaMarketSearch("Water Filter")
            #buys with an offset of 3 to try and prevent low count filters
            self.buyOnFlea(1, "Water Filter", 8) 
            self.locateNode('water')
            self.clickMidLeft() 
            if pygui.locateOnScreen("WaterLoader_gene.png", confidence=0.9) == None:
                print("Error 0006: Water func unknown failure")
                pygui.press("esc")
                return "fail"
            _water_x, _water_y = pygui.locateCenterOnScreen("Water_gene.png", confidence=0.9)
            pygui.click(x=_water_x, y=_water_y)
            print("Water filter successfully added...")
            pygui.press("esc")
        else:
           _water_x, _water_y = pygui.locateCenterOnScreen("Water_gene.png", confidence=0.9)
           pygui.click(x=_water_x, y=_water_y)
           print("Water filter successfully added...")
           pygui.press("esc")
           
           
    def gcardBuyAndAdd(self, count=1):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        #buys a graphics card and adds it to btc farm 
        self.bottomFlea()
        self.fleaMarketSearch('Graphics Card')
        self.buyOnFlea(1, 'Graphics Card', 1) 
        self.locateNode('btc')
        pygui.click(x=1272, y=712)
        pygui.press('esc')
        
        
    def runScavCase(self, item):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        #item is which scav case item to run
            #MOON, 950, 25, 150, INTEL
        self.locateNode("scav")
        scav_names = ["MOON", "950", "25", "150", "INTEL"]
        if item in scav_names:
            item_full_name = self.scav_names[item]
            if pygui.locateOnScreen(item + "_status.png", confidence=0.925) != None:
                self.startRecipe(item, "scav")
                print("Scav case started with " +item+ "...")
                return
            if item == "MOON" or item == "INTEL":   
                self.bottomFlea()
                self.fleaMarketSearch(1,item_full_name)
                self.buyOnFlea(1, item_full_name)
                self.locateNode("scav")
                self.startRecipe(item, "scav")
                pygui.press("esc")
                return
            else:
                print("Not enough roubles to run " + item_full_name + " scav case")
                return 'fail'
        else:
            print("ERROR: Invalid item passage")
            return 'fail'
        
        
    def goToMessenger(self):
        if pygui.locateCenterOnScreen("messenger_button.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("messenger_button.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(0.25)
        else:
            print("Error. No messenger button found. Flea claim failed")
            return "fail"
        
        
    def checkReceive(self):
        if pygui.locateCenterOnScreen("ReceiveAll_claim.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("ReceiveAll_claim.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(1.25)
            if pygui.locateCenterOnScreen("ReceiveAll2_claim.png", confidence=0.8) != None:
                point_x, point_y = pygui.locateCenterOnScreen("ReceiveAll2_claim.png", confidence=0.8)
                pygui.click(x=point_x, y=point_y)
                sleep(0.25)
                if pygui.locateCenterOnScreen("NoSpace_status.png", confidence=0.9) != None:
                    #this means you couldn't claim items
                     print("No space to claim items. Fatal error")
                     return "FATAL"
                sleep(0.5)
                if pygui.locateCenterOnScreen("Accept_claim.png", confidence=0.9) != None:
                    point_x, point_y = pygui.locateCenterOnScreen("Accept_claim.png", confidence=0.9)
                    pygui.click(x=point_x, y=point_y)
                    sleep(0.5)
                    pygui.press('y')
                    print("All flea items successfully claimed")
                    sleep(0.5)
                else:
                    print("Error: No Acceptance found. Bad bug")
                    return "FATAL"
            else:
                print("Error: 2nd receive button not found")
                return "FATAL"
        else:
            sleep(0.5)
            return 'fail'
        
        
    def claimFlea(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        
        os.chdir(self.submenu_path)
        if self.goToMessenger() == "fail":
            return "fail"
        
        if pygui.locateCenterOnScreen("RagmanActive_selection.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("RagmanActive_selection.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(0.25)
        elif pygui.locateCenterOnScreen("RagmanInactive_selection.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("RagmanInactive_selection.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(0.25)
        else:
            print("Error: Ragman not found. Flea claim failed")
            return "fail"
        
        status = self.checkReceive()
        if status == "fail":
            print("No flea items to claim")
        elif status == "FATAL":
            print("Error:Flea claim Fatal error")
            return "FATAL"

    
    def claimInsurance(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        
        #checks prapor then therapist
        
        os.chdir(self.submenu_path)
        if self.goToMessenger() == "fail":
            return "fail"
        
        if pygui.locateCenterOnScreen("PraporActive_selection.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("PraporActive_selection.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(0.25)
        elif pygui.locateCenterOnScreen("PraporInactive_selection.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("PraporInactive_selection.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(0.25)
        else:
            print("Error: Prapor not found. Flea claim failed")
            return "fail"
        
        status_1 = self.checkReceive()
        if status_1 == "fail":
            print("No items to claim from Prapor")
        elif status_1 == "FATAL":
            return "FATAL"
        else:
            print("Claimed items from Prapor")
            return
        
        if pygui.locateCenterOnScreen("TherapistActive_selection.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("TherapistActive_selection.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(0.25)
        elif pygui.locateCenterOnScreen("TherapistInactive_selection.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("TherapistInactive_selection.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(0.25)
        else:
            print("Error: Therapist not found. Flea claim failed")
            return "fail"
        
        status_2 = self.checkReceive()
        if status_2 == "fail":
            print("No items to claim from Therapist")
            print("No insurance to claim at all")
        elif status_2 == "FATAL":
            return "FATAL"
        else:
            print("Claimed items from Therapist")
            return
           
            
        
        
    #not used rn
    def checkForPrompt(self, claim="yes"):
        #checks for a prompt on screen. presses yes by default
        if pygui.locateOnScreen("confirmation_status.png", confidence=0.9) != None and pygui.locateOnScreen("yesno_button.png", confidence=0.9) != None:
            if claim == "yes":
                point_x, point_y = pygui.locateCenterOnScreen("yes_button.png", confidence=0.9)
                pygui.click(x=point_x, y=point_y)
            elif claim == "no":
                point_x, point_y = pygui.locateCenterOnScreen("no_button.png", confidence=0.9)
                pygui.click(x=point_x, y=point_y)
            else:
                print("Error: Invalid claim input")
                return
        
        

 
 
                          
        
        
 