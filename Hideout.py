# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:22:17 2022

@author: vinch
"""

#Hideout v2
 

#Hideout v2

#<><><><><><><><>
#---------------
#TarkovBotV2
#---------------
#<><><><><><><><>

#Use sentiment to define photo groups (Ready to go, Unable to go etc.)
#THIS IS ARROW STRAT
 
import pyautogui as pygui
from time import sleep
import random
import cv2
import os 
#_icon = status
#_stamp = buttons
#_node = node
 
#NODE STATUSES 
    #Under Construction (construction_icon) (grab time left)
    #Producing (production_icon) (grab time left)
    #Farming (farming_icon) (Grab time left, only for btc) (may wanna make farming and producing together)
    #Inactive (Lack of any) (Start with one recipe (BP) and have that auto renew ) (check for start_ready_icon and if visible, check if all bp components visible too)
    #Items Ready (item_ready_icon) (Should save the name of whats being constructed so you dont have to check everytime)
#HIDEOUT STATUSES
    #No fuel (no_fuel_icon)
#LEVELS
    #level_2_icon
    

 
class Hideout:
    
    def __init__(self):

        self.base_path = os.getcwd()
        #goes to "Icons" Folder
        self.stamp_path = os.path.join(self.base_path, 'Icons')
        #goes to "Nodes" Folder within "Icons"
        self.icons_path = os.path.join(self.stamp_path, 'Nodes')
        #goes to "Blocks" Folder
        self.blocks_path = os.path.join(self.base_path, 'Blocks')
        #goes to "Node_Descriptions" within "Icons"
        self.descriptions_path = os.path.join(self.stamp_path, 'Node_Descriptions')
        #item icons path
        self.item_path = os.path.join(self.stamp_path, "Item_Icons")
        #submenu options path
        self.submenu_path = os.path.join(self.stamp_path, "Submenu_Options")
        #recipes path
        self.recipes_path = os.path.join(self.stamp_path, "Recipes") 
        
        # self.statuses = ["working_full_node", "working_empty_node", "working_half_node", "incomplete_node", "na_node", "locked_node", "complete_node", "unpowered_node"] 
        self.node_names = ["air", "booze", "btc", "generator", "heating", "illumination", "intel", "lav", "library", "med", "nutrition", "rest", "scav", "vents", "water", "workbench"] 
        self.current_statuses = []
        
    #<><><><><><><><><><><><><>
    #Simple Hideout Functions 
    #<><><><><><><><><><><><><>
    
    def goToHideout(self):
        #Click "Hideout" (Bottom)
        pygui.click(x=201, y=1057)
        #Sleeps 10 so hideout has enough time to load 
        #sleep(10)
        #ADD  SELF VAR THAT HOLDS HIDOUT LOAD STATUS
        
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
    #Passive Hideout Functions
    #<><><><><><><><><><><><><>
    
    def findStatus(self, icon_list):
        #Moves you to
        os.chdir(self.stamp_path)
        #Assumes you are already in a node
        #returns icon file name if valid, None if not 
        for icon in icon_list:
            print(icon)
            if pygui.locateOnScreen(icon, confidence=0.8) != None:
                icon_split = icon.split('_')
                return icon_split[0]
        return "Inactive"    
            
    def findNodeName(self, description_list):
        #Assumes you are already in a node
        #returns node name, None if not found
        os.chdir(self.descriptions_path)
        for node in description_list: 
            if pygui.locateOnScreen(node, confidence=0.9):
                node_split = node.split("_") 
                #return the nodes name, splits it at _ 
                return node_split[0]       
 
    def findAllStatuses(self):
        #WORKING
        self.goToHideout()
        sleep(10)
        #goes to icons path, says there after funct complete
        os.chdir(self.stamp_path) 
        #grab directory contents (specifically files)
        dir_contents = [f for f in os.listdir('.') if os.path.isfile(f)]
        #grabs only status icons 
        icon_contents = [f for f in dir_contents if "_icon" in f.lower()]
        #move to description dir
        os.chdir(self.descriptions_path)
        desc_dir_contents = [f for f in os.listdir('.') if os.path.isfile(f)] 
        #grabs only file names w/ description
        node_descriptions = [f for f in desc_dir_contents if "_description" in f.lower()] 
        #Clicks bottom left node
        pygui.click(x=151, y=998)
        name_and_status = {} 
        for i in range(20): 
            _status = self.findStatus(icon_contents)
            _name = self.findNodeName(node_descriptions)
            name_and_status[_name] = _status 
            pygui.click(x=1874, y=997) 
            sleep(0.5)
        return name_and_status
    
 
    
 
    
 
    #<><><><><><><><><><><><><>
    #Active Hideout Functions
    #<><><><><><><><><><><><><>
    
    #currently, all functions here made to support makeBP() 
    # def clickToFilter(self, file_dir, file_name):
    #     os.chdir(file_dir)
    #     #Assumes you can see item  
    #     item_location = pygui.locateOnScreen(file_name, confidence=0.9)
    #     if item_location != None: 
    #         itemx, itemy = pygui.center(item_location) 
    #         pygui.rightClick(x=itemx, y=itemy)
    #         sleep(0.25)
    #         os.chdir(self.submenu)
    #         filter_location = pygui.locateOnScreen("FilterByItem_Option.png", confidence=0.9)
    #         if filter_location != None:
    #             filterx, filtery = pygui.center(filter_location)
    #             pygui.click(filterx, filtery)
    #             sleep(0.5)
    #         else:
    #             print("ERROR: Somehow the filter isnt there")
    #             return "fail"
    
    def bottomFlea(self):
        pygui.click(x=1228, y=1066)
        sleep(1)
    
    def buyAid(self, offset=None):
        #assumes you are on flea  
        #FIRST PURCHASE POINT (x=1761, y=179)
        #offset is an int for jumping down a certain count 
        if offset == None or offset == 0:
            pygui.click(x=1761, y=179)
            sleep(0.15)
            pygui.press("y")
            sleep(0.5)
        else:
            pixel_offset = 72 * offset
            pygui.click(x=1762, y=179+pixel_offset)
            sleep(0.15)
            pygui.press("y")
            sleep(0.5)
       
    def buyOnFlea(self, count, item_name, offset=None):  
        _index = 0
        _z = 0
        os.chdir(self.submenu_path)
        while _index < count and _z < 6:
            self.buyAid(offset)
            if pygui.locateOnScreen("PurchaseComplete_option.png", confidence=0.7) != None:
                _index += 1
                sleep(2.25)
            else:
                print("Purchase failed, retrying")
                _z += 1
        if _z == 6:
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
        pygui.click(x=187, y=164)
        sleep(1)
        
    def checkAndBuyRecipe(self, repeat_names, item_info):
        #EXPECTS YOU TO HAVE ALREADY MOVED TO IT ON SCREEN
        #repeat names is a list of the names of the repeatable items as seen in the item_icon folder 
        #if name+ready_item...png found, don't add to list
        #if not ready found, add to list
        #if neither found, throw error
        #item_info is a dict. item_name:item_count
        #ADD BUY STACK FUN
        base_item_info = item_info
        
        #this checks if repeat items need to be added to shopping list
        
        if len(repeat_names) > 3:
            print("Error 0001: Repeat items are never higher than 3")
            return 
        
        os.chdir(self.item_path)
        
        for name in repeat_names:
            #This needs to still exist but just check status
            if pygui.locateOnScreen(str(name)+"Ready_item_icon.png", confidence=0.9) != None:
                print(str(name) + ' is already bought')
                continue
            elif pygui.locateOnScreen(str(name)+"NotReady_item_icon.png", confidence=0.9) != None:
                print(str(name) + ' added to shopping list')
                item_info[name] = 1
            else:
                print("Error 0000: Item not on screen, defaulting to add to shopping list")
                item_info[name] = 1
                continue
            
        print("<><><><><><><><><><>")
        print("Shopping list ready")
        print("---------------------")
        print(item_info)
        print("<><><><><><><><><><>")

        self.bottomFlea()
        sleep(1)        
                
        for name, count in item_info.items():
            _name = name
            if "-" in _name:
                #adds quotes to names that need quotes
                #may not need, as file names aren't being passed
               _name = _name.replace("-", "\"" )
            self.fleaMarketSearch(_name)
            self.buyOnFlea(count, _name)        
            sleep(1)    
     
    def reusableExitLoop(self, item_name):
        #item name is a string to a .png
        #img should be of item + count and a side recipe item to confirm its at the right one
        #NEED TO TEST SCROLL COUNT
        _exit = False
        _i = 0
        while _exit == False:
            os.chdir(self.item_path)
            if pygui.locateOnScreen(item_name , confidence=0.9) != None: 
                _exit = True
            if _i > 20:
                print("No item found")
                return None
            _i += 1
            pygui.moveTo(x=1410, y=655) 
            pygui.scroll(-100)
            print('scrolled') 
            sleep(0.25)
            
    def locateWorkbench(self):
        #returns True if workbench located, False if not
        #ASSUMES YOU ARE IN HIDEOUT         
        #list of all workbench satus img files
        os.chdir(self.icons_path)
        workbench_list = [f for f in os.listdir('.') if os.path.isfile(f) and "workbench" in f.lower()] 
        self.hideoutMoveLeft()
        for node in workbench_list:
            if pygui.locateOnScreen(node, confidence=0.75) != None:
                #clicks to workbench
                node_loc = pygui.locateOnScreen(node, confidence=0.7)
                node_point = pygui.center(node_loc)
                nodex, nodey = node_point
                pygui.click(x=nodex, y=nodey)
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
        
    def makeRecipe(self, recipe):
        
        #untested, good start though
        #currently only does workbench
        
        #recipe is a dict
            #{"item_name": item_name , "repeats":[str1,str2*,str3*] , "item_info":{_item_name:item_count} , "start":"item_nameStart_Recipe.png" }
        #NEED TO CHANGE TO MATCH CURRENT STRUCTURE
            #current : {recipe_name:{Ingredient_1:count, Ingredient_2:count}}
            #need to take start pics
                #may be able to edit together item photo and start next to it to avoid having to get items
        
        #Takes you to hideout from home screen
        self.returnToMainMenu()
        self.goToHideout()
        sleep(0.5) 
        
        workbench = self.locateWorkbench()
        
        if workbench == True:
                
            sleep(1)
            os.chdir(self.item_path) 
            self.reusableExitLoop()
            
            #then need to check if recipe completely ready (use an img of recipe w/ white start next to it)
            #if ready, just actiavte
            
            self.checkAndBuyRecipe(recipe["repeats"], recipe["item_info"]) 
            
            self.goToHideout()
            _workbench = self.locateWorkbench()
            if _workbench == True:
                self.reusableExitLoop()
                os.chdir(self.recipes_path)
                item_loc = pygui.locateOnScreen(recipe["start"], confidence=0.9) 
                if item_loc != None:
                    pygui.click(pygui.center(item_loc))
                    sleep(0.1)
                    pygui.press("y")
                    print("Recipe for " + str(recipe["item_name"] + " successfully started"))
                    #successful start
                    return None
                else:
                    print("Error 0003: No " + str(recipe["item_name"] + " start found"))
                    return "fail"
            
            else:
                print("Error 0002: No workbench node found. Exiting... ")
                return "fail" 
        else:
            print("Error 0002: No workbench node found. Exiting... ")
            return "fail"
 
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
        first_loc = pygui.locateOnScreen("NoFuel_gene.png")
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
        
    def goToGenerator(self):
        self.goToHideout()
        self.hideoutReset()
        os.chdir(self.icons_path)
        generator_images = [f for f in os.listdir('.') if "generator" in f]
        for image in generator_images:
            if pygui.locateOnScreen(image, confidence=0.9) != None:
                generator_loc = pygui.locateOnScreen(image, confidence=0.9)
                generator_x, generator_y = pygui.center(generator_loc)
                pygui.click(x=generator_x, y=generator_y)
                return
        print("Error 0005: Generator not found")
        return 'fail'    
  
    def generatorChecker(self):
        #Checks if generator has room for more fuel, adds or buys and adds if needed
        #generator images in submenu, _gene
        self.goToGenerator()
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
            jaeger_offer_loc_x, jaeger_offer_loc_y = pygui.locateCenterOnScreen("JaegerFuelPrice_gene.png", confidence=0.9) 
            purchase_loc_x = jaeger_offer_loc_x + 350
            pygui.click(x=purchase_loc_x, y=jaeger_offer_loc_y)
            sleep(0.1)
            pygui.press('y')
            pygui.press('y')
            print("Large Fuel Successfully Purchased")
            #can fail if sold out or not enough $
            sleep(0.5)
            self.goToGenerator()
            self.clickMidLeft()
            fuel_loc_x, fuel_loc_y = pygui.locateOnScreen("BigFuelFull_gene.png", confidence=0.9)
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Large Fuel Loaded")
            return
   
    def goToWater(self):
        self.goToHideout()
        self.hideoutReset()
        os.chdir(self.icons_path)
        water_pics = [f for f in os.listdir('.') if "water_" in f]
        for pic in water_pics:
            if pygui.locateOnScreen(pic, confidence=0.9) != None:
                water_x, water_y = pygui.locateCenterOnScreen(pic, confidence=0.9) 
                pygui.click(x=water_x, y=water_y)
                sleep(0.5)
                return
        print("Error 0007: Water node not found ")
        return "fail"        
    
    def waterChecker(self):
        #all checkers auto load and buy if empty 
        self.goToWater()
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
            self.goToWater()
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
    
    def goToBooze(self):
        self.goToHideout()
        self.hideoutReset()
        os.chdir(self.icons_path)
        booze_pics = [f for f in os.listdir('.') if "booze_" in f]
        for pic in booze_pics:
            if pygui.locateOnScreen(pic, confidence=0.9) != None:
                booze_x, booze_y = pygui.locateCenterOnScreen(pic, confidence=0.9)
                pygui.click(x=booze_x, y=booze_y)
                sleep(0.5)
                return
        print("Error 0008: Booze node not found somehow")
        return "fail"
    
    def boozeChecker(self):
        
        #NEEDS STATUS PICS
        
        self.goToBooze()
        
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
            
        self.goToBooze() 
        
        if pygui.locateOnScreen("StartStatus.png", confidence=0.9) == None:
            print("Error 0009: No start found")
            return "fail"
        start_x, start_y = pygui.locateCenterOnScreen("StartStatus.png", confidence=0.9)
        pygui.click(x=start_x, y=start_y)
        sleep(0.25)
        pygui.press('y')
        print('Successfully began moonshine production...')
        return 
 
    def goToAir(self):
        #NOTE: no pics exist for this, need to take pics
        self.goToHideout()
        self.hideoutReset()
        os.chdir(self.icons_path)
        air_pics = [f for f in os.listdir('.') if "air_" in f]
        for pic in air_pics:
            if pygui.locateOnScreen(pic, confidence=0.9) != None:
                air_x, air_y = pygui.locateCenterOnScreen(pic, confidence=0.9)
                pygui.click(x=air_x, y=air_y)
                sleep(0.5)
                return
        print("Error 0010: Booze node not found somehow")
        return "fail"
    
    def airChecker(self):
        self.goToAir()
        
        os.chdir(self.submenu_path)
        
        if pygui.locateOnScreen("NoFuel_gene.png", confidence=0.9) == None:
            print("Air filter currently loaded and running...")
            return
        self.clickMidLeft()
        if pygui.locateOnScreen("NoFuelLoader_gene.png", confidence=0.9) != None:
            print("No spare air filters. Buying one from market...")
            self.bottomFlea()
            self.fleaMarketSearch("FP-100 Filter Absorber") 
            self.buyOnFlea(1, "FP-100 Filter Absorber")  
            self.goToAir()
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
           
        
        
        
 