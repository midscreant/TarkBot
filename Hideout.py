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
    
    def __init__(self):

        self.base_path = os.getcwd()
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
 
        #initial hideout press
        self.initial = False
        
        #lists of dicts
            #dicts are recipe books {recipe_name:{ingredient_1:count, ...}} 
        self.workbench_recipes = all_recipes["Workbench"]
        self.nutrition_recipes = all_recipes["Nutrition"]
        self.intel_recipes = all_recipes["Intel"]
        self.medstation_recipes = all_recipes["Medstation"]
        
        #complete dicts
        self.full_workbench_recipes = self.workbench_recipes[0] | self.workbench_recipes[1] | self.workbench_recipes[2] 
        self.full_nutrition_recipes = self.nutrition_recipes[0] | self.nutrition_recipes[1] | self.nutrition_recipes[2]
        self.full_intel_recipes = self.intel_recipes[0] | self.intel_recipes[1] 
        self.full_medstation_recipes = self.medstation_recipes[0] | self.medstation_recipes[1] | self.medstation_recipes[2]
        
        #name dicts
        self.workbench_names = all_recipes["Workbench - Names"]
        self.nutrition_names = all_recipes["Nutrition - Names"]
        self.intel_names = all_recipes["Intel - Names"]
        self.medstation_names = all_recipes["Medstation - Names"]
        self.scav_names = all_recipes["Scav - Names"]
        
    #<><><><><><><><><><><><><>
    #Simple Hideout Functions 
    #<><><><><><><><><><><><><>
    
    def goToHideout(self):
        #Click "Hideout" (Bottom)
        pygui.click(x=201, y=1057)
        if self.initial == False: 
            self.initial = True
            sleep(10)
        sleep(0.5)    
 
    
    def hideoutReset(self): 
        #reset to middle
        pygui.press('enter')
        sleep(1) 
        pygui.press('esc')
        sleep(0.25)
         
        
    def hideoutMoveLeft(self):
        self.hideoutReset()
        #Move left 
        pygui.moveTo(x=1,y=540)
        sleep(0.3)
        pygui.moveTo(x=960,y=540)
        sleep(0.3)
        
        
    def hideoutMoveRight(self):
        self.hideoutReset()
        #Move right
        pygui.moveTo(x=1919,y=540)
        sleep(3)
        pygui.moveTo(x=960,y=540) 
        sleep(0.3)
 
    #<><><><><><><><><><><><><>
    #Active Hideout Functions
    #<><><><><><><><><><><><><>
 
    def bottomFlea(self):
        pygui.click(x=1228, y=1066)
        sleep(0.5)
    
    def startRecipe(self, item_pic_name, node_name, status=None):
        
        if node_name == "med": 
            os.chdir(self.medstation_recipes_path)
        elif node_name == "intel": 
            os.chdir(self.intel_recipes_path)
        elif node_name == "nutrition": 
            os.chdir(self.nutrition_recipes_path)
        elif node_name == "workbench": 
            os.chdir(self.workstation_recipes_path)
        elif node_name == "scav": 
            os.chdir(self.scav_recipes_path)
        # item_loc = None
        # if status != None:
        #     item_loc = pygui.locateOnScreen(item_pic_name + "_status.png", confidence=0.925)
        # else:    
        item_loc = pygui.locateOnScreen(item_pic_name + "_recipe.png", confidence=0.925) 
        if item_loc != None:
            item_left_x = item_loc.left
            item_width = item_loc.width 
            item_x, item_y = pygui.center(item_loc) 
            #shift 72 pixels right to click start button
            pygui.click(x=item_left_x + item_width + 72, y=item_y)
            sleep(0.1)
            pygui.press("y")
            #Should add a confirmation check here
            print("Recipe for " + item_pic_name + " successfully started") 
            #successful start
            return
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
                sleep(0.1)
                pygui.click(x=1045, y=482)
                sleep(0.1)
                pygui.write(str(count), interval=0.075)
                sleep(0.1)
                pygui.press("y")
                sleep(0.5)
            else:    
                pixel_offset = 72 * offset
                pygui.click(x=1762, y=179+pixel_offset)
                sleep(0.1)
                pygui.click(x=1045, y=482)
                sleep(0.1)
                pygui.write(str(count), interval=0.075)
                sleep(0.1)
                pygui.press("y")
                sleep(0.5) 
        elif offset == None or offset == 0:
            pygui.click(x=1761, y=179)
            sleep(0.1)
            pygui.press("y")
            sleep(0.5)
        else:
            pixel_offset = 72 * offset
            pygui.click(x=1762, y=179+pixel_offset)
            sleep(0.1)
            pygui.press("y")
            sleep(0.5)
       
        
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
            if count > 10:
                #moves to stack purchase
                self.buyAid(count, offset)
            else:
                self.buyAid(offset=offset) 
            if pygui.locateOnScreen("PurchaseComplete_option.png", confidence=0.7) != None:
                _index += 1
                if count > 10:
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
            print("All "  + str(count) + " " + item_name + "s bought")       
 
    
    def fleaMarketSearch(self, item_name):
        #assumes you are already on the flea
        #assumes you already have a specific item selected 
        #click text box 
        pygui.click(x=258, y=121)
        pygui.write(item_name, interval=0.125)
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
            #these items were problomatic so added extra check
            pygui.click(x=155, y=234)
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
        recipe_tuple, recipe_pic_name = self.findRecipe(item_name)
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
            os.chdir(self.workstation_recipes_path)
        elif node_name == "scav":
            _exit_count = 15
            os.chdir(self.scav_recipes_path)
        else:
            print("Error: Invalid node name passed")
            return 'fail'
        while _exit == False: 
            if pygui.locateOnScreen(recipe_pic_name + "_recipe.png", confidence=0.9) != None: 
                _exit = True
            if _i > _exit_count:
                print("No item found after " + str(_exit_count) + " attempts")
                return None
            _i += 1
            pygui.moveTo(x=1410, y=655) 
            pygui.scroll(-4000)
            print('scrolled') 
 
    
    def locateNode(self, node_name):
        self.goToHideout()
        #add
        #node names - "med", "nutrition", "workbench", "intel"
            #right left node list
        right_nodes = ["heating", "library", "rest", "med", "air", "nutrition", "booze", "water"]
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
            if pygui.locateOnScreen(file, confidence=0.8) != None:
                node_x, node_y = pygui.locateCenterOnScreen(file, confidence=0.8)
                pygui.click(x=node_x, y=node_y)
                print(node_name + " found and clicked...")
                return True
        return False    
    
    
    def returnToMainMenu(self):
        pygui.press('esc')
        sleep(0.1)
        pygui.press('esc')
        sleep(0.1)
        pygui.press('esc')
        sleep(0.1)
        pygui.press('esc') 
        sleep(0.5)
    
    
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
            dir_2 = self.full_workbench_recipes 
        elif node_name == "med":
            dir_1 = self.medstation_names
            dir_2 = self.full_medstation_recipes 
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
        node_name = " "
        if recipe_name in list(self.full_workbench_recipes):
            node_name = "workbench"
        elif recipe_name in list(self.full_nutrition_recipes):
            node_name = "nutrition"
        elif recipe_name in list(self.full_intel_recipes):
            node_name = "intel"
        elif recipe_name in list(self.full_medstation_recipes):
            node_name = "med"    
        else:    
            print("Error: recipe not found, so no node can be pressed")
            return 'fail'
 
        #basic testing complete
        #need to test confidence levels
        #error checking is next big step
        self.returnToMainMenu()
        self.goToHideout()
        sleep(0.5)  
        node_located = self.locateNode(node_name) 
        if node_located == True:   
            sleep(1) 
            self.reusableExitLoop(recipe_name, node_name) 
            recipe_tuple, recipe_pic_name = self.findRecipe(recipe_name, node_name)
            _recipe_name, recipe_value = recipe_tuple 
            self.checkAndBuyRecipe(recipe_value)  
            self.goToHideout()
            _node_located = self.locateNode(node_name)
            if _node_located == True:
                self.reusableExitLoop(recipe_name, node_name)
                self.startRecipe(recipe_pic_name, node_name)
            else:
                print("Error 0002: No workbench node found. Exiting... ")
                return "fail" 
        else:
            print("Error 0002: No workbench node found. Exiting... ")
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
        
        
    def clickMidLeft(self):
        first_loc = pygui.locateOnScreen("NoFuel_gene.png", confidence=0.95)
        #moving to mid left of button
        _left, _top, _width, _height = first_loc
        _height = _height/2
        _width = _width - 5
        point_x = _left + _width
        point_y = _top + _height
        pygui.click(x=point_x, y=point_y)
        sleep(0.25)
        
        
    def quickOrganizeInv(self):
        self.returnToMainMenu()
        #click bottom character
        pygui.click(x=960, y=1064)
        sleep(0.25)
        #click auto-sort and confirm
        pygui.click(x=1244, y=922)
        sleep(0.25)
        pygui.press('y')  
 
    #will need to make air filter to test
    
    
    def airChecker(self):
        self.locateNode('air') 
        os.chdir(self.submenu_path) 
        #CHANGE NoFuel_gene.png to AirFilterIN (need to create)
        if pygui.locateOnScreen("NoFuel_gene.png", confidence=0.9) == None:
            print("Air filter currently loaded and running...")
            return
        self.clickMidLeft()
        if pygui.locateOnScreen("NoFuelLoader_gene.png", confidence=0.9) != None:
            print("No spare air filters. Buying one from market...")
            self.bottomFlea()
            self.fleaMarketSearch("FP-100 Filter Absorber") 
            self.buyOnFlea(1, "FP-100 Filter Absorber")  
            self.locateNode('air')
            self.clickMidLeft() 
            if pygui.locateOnScreen("AirLoader_gene.png", confidence=0.9) == None:
                print("Error 0011: Air func unknown failure")
                return "fail"
            _air_x, _air_y = pygui.locateCenterOnScreen("Air_gene.png", confidence=0.9)
            pygui.click(x=_air_x, y=_air_y)
            print("Air filter successfully added...")
        else:
           _air_x, _air_y = pygui.locateCenterOnScreen("Air_gene.png", confidence=0.9)
           pygui.click(x=_air_x, y=_air_y)
           print("Air filter successfully added...")
           
      
    def boozeChecker(self): 
        #NEEDS STATUS PICS 
        self.locateNode('booze')
        os.chdir(self.submenu_path) 
        if pygui.locateOnScreen("BoozeProducingStatus.png", confidence=0.9) != None:
            print("Booze currently being produced...")
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
            sleep(0.5)           
        if sugar_count > 0:
            self.goToHideout()
            self.bottomFlea()
            self.fleaMarketSearch("Pack of sugar")
            self.buyOnFlea(sugar_count, "Pack of sugar", 3)
            sleep(0.5)  
        self.locateNode('booze') 
        if pygui.locateOnScreen("StartStatus.png", confidence=0.9) == None:
            print("Error 0009: No start found")
            return "fail"
        start_x, start_y = pygui.locateCenterOnScreen("StartStatus.png", confidence=0.9)
        pygui.click(x=start_x, y=start_y)
        sleep(0.25)
        pygui.press('y')
        print('Successfully began moonshine production...')
        return
    
    
    def btcChecker(self):
        #deals with btc not graphics
        self.locateNode('btc')
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("GetItemsStatus.png", confidence=0.9) != None:
            status_x, status_y = pygui.locateOnScreen("GetItemsStatus.png", confidence=0.9)
            pygui.click(x=status_x, y=status_y)
            print("Bitcoins claimed...") 
        print('No bitcoins to be claimed...')
       

    def generatorChecker(self):
        #Checks if generator has room for more fuel, adds or buys and adds if needed
        #generator images in submenu, _gene
        self.locateNode('generator')
        os.chdir(self.submenu_path) 
        #listing loader imgs
        if pygui.locateOnScreen("BigFuelLoader_gene.png", confidence=0.9) != None:
            fuel_loc_x, fuel_loc_y = pygui.locateCenterOnScreen("BigFuelFull_gene.png")
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Large Fuel Loaded")
            #Then grab updated time left
            sleep(0.5)
            return
        elif pygui.locateOnScreen("SmallFuelLoader_gene.png", confidence=0.9) != None:
            fuel_loc_x, fuel_loc_y = pygui.locateCenterOnScreen("SmallFuelFull_gene.png")
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Small Fuel Loaded")
            #Then grab updated time left
            sleep(0.5)
            return
        else:
            self.fleaMarketSearch("Metal Fuel Tank") 
            fuel_loc = pygui.locateOnScreen("JaegerFuelPrice_gene.png", confidence=0.9)
            fuel_point_x, fuel_point_y = pygui.center(fuel_loc)
            fuel_left_x = fuel_loc.left 
            purchase_loc_x = fuel_left_x + fuel_loc.width + 275
            pygui.click(x=purchase_loc_x, y=fuel_point_y)
            sleep(0.1)
            pygui.press('y') 
            print("Large Fuel Successfully Purchased")
            #can fail if sold out or not enough $. Add check
            sleep(0.5)
            self.locateNode('generator')
            self.clickMidLeft()
            fuel_loc_x, fuel_loc_y = pygui.locateOnScreen("BigFuelFull_gene.png", confidence=0.9)
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Large Fuel Loaded")
            return     
        
    
    def waterChecker(self):
        #all checkers auto load and buy if empty 
        self.locateNode('water')
        os.chdir(self.submenu_path)
        #if there's already a filter loaded, function ends
        if pygui.locateOnScreen("NoFuel_gene.png", confidence=0.9) == None:
            print("Water filter currently loaded and running...")
            return
        self.clickMidLeft()
        #if there's no water filters ready to be loaded, buy one on market
        if pygui.locateOnScreen("NoFuelLoader_gene.png", confidence=0.9) != None:
            print("No spare water filters. Buying one from market...")
            self.bottomFlea()
            self.fleaMarketSearch("Water Filter")
            #buys with an offset of 3 to try and prevent low count filters
            self.buyOnFlea(1, "Water Filter", 3) 
            self.locateNode('water')
            self.clickMidLeft() 
            if pygui.locateOnScreen("WaterLoader_gene.png", confidence=0.9) == None:
                print("Error 0006: Water func unknown failure")
                return "fail"
            _water_x, _water_y = pygui.locateCenterOnScreen("Water_gene.png", confidence=0.9)
            pygui.click(x=_water_x, y=_water_y)
            print("Water filter successfully added...")
        else:
           _water_x, _water_y = pygui.locateCenterOnScreen("Water_gene.png", confidence=0.9)
           pygui.click(x=_water_x, y=_water_y)
           print("Water filter successfully added...")
           
           
    def gcardBuyAndAdd(self, count=1):
        #buys a graphics card and adds it to btc farm 
        self.bottomFlea()
        self.fleaMarketSearch('Graphics Card')
        self.buyOnFlea(1, 'Graphics Card', 1) 
        self.locateNode('btc')
        pygui.click(x=1272, y=712)
        pygui.press('esc')
        
    def runScavCase(self, item):
        #item is which scav case item to run
            #MOON, 950, 25, 150, INTEL
        self.locateNode("scav")
        scav_names = ["MOON", "950", "25", "150", "INTEL"]
        if item in scav_names:
            item_full_name = self.scav_names[item]
            if pygui.locateOnScreen(item + "_status.png", confidence=0.925) != None:
                self.startRecipe(item, "scav")
                return
            if item == "MOON" or item == "INTEL":   
                self.bottomFlea()
                self.fleaMarketSearch(1,item_full_name)
                self.buyOnFlea(1, item_full_name)
                self.locateNode("scav")
                self.startRecipe(item, "scav")
                return
            else:
                print("Not enough roubles to run " + item_full_name + " scav case")
                return
        else:
            print("ERROR: Invalid item passage")
            return 'fail'               
        
        
 