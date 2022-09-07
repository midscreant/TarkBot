# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:26:40 2022

@author: vinch
"""

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
        self.submenu = os.path.join(self.stamp_path, "Submenu_Options")
        #recipes path
        self.recipes = os.path.join(self.stamp_path, "Recipes") 
        
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
        
    def hideoutReset(self): 
        #reset to middle
        pygui.press('enter')
        sleep(1)
        print('wtf')
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
    
    def clickToFilter(self, file_dir, file_name):
        os.chdir(file_dir)
        #Assumes you can see item  
        item_location = pygui.locateOnScreen(file_name, confidence=0.9)
        if item_location != None: 
            itemx, itemy = pygui.center(item_location) 
            pygui.rightClick(x=itemx, y=itemy)
            sleep(0.25)
            os.chdir(self.submenu)
            filter_location = pygui.locateOnScreen("FilterByItem_Option.png", confidence=0.9)
            if filter_location != None:
                filterx, filtery = pygui.center(filter_location)
                pygui.click(filterx, filtery)
                sleep(0.5)
            else:
                print("ERROR: Somehow the filter isnt there")
                return "fail"
       
    def buyAid(self):
        #assumes you are on flea  
        #FIRST PURCHASE POINT (x=1761, y=179) 
        pygui.click(x=1761, y=179)
        sleep(0.15)
        pygui.press("y")
        sleep(0.5) 
       
    def buyOnFlea(self, count):  
        _index = 0
        _z = 0
        os.chdir(self.submenu)
        while _index < count and _z < 6:
            self.buyAid()
            if pygui.locateOnScreen("PurchaseComplete_option.png", confidence=0.7) != None:
                _index += 1
                sleep(2.25)
            else:
                print("Purchase failed, retrying")
                _z += 1
        if _z == 6:
            print("some or all failed")
            sleep(0.25)
            return "fail"
        else:
            sleep(0.25)
            print("all bought") 
 
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
        os.chdir(self.submenu)
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
     
    def reusableBPExitLoop(self):
        _exit = False
        _i = 0
        while _exit == False:
            os.chdir(self.item_path)
            if pygui.locateOnScreen("762bp_item_icon.png", confidence=0.9) != None: 
                _exit = True
            if _i > 12:
                print("No item found")
                return None
            _i += 1
            pygui.moveTo(x=1410, y=655) 
            pygui.scroll(-35)
            print('scrolled') 
            sleep(0.5)
        
    def makeBp(self):
        #WORKING
        #MAKE GENERAL PURPOSE
        #Takes you to hideout from home screen
        pygui.press('esc')
        sleep(0.5)
        self.goToHideout()
        sleep(0.5) 
        os.chdir(self.icons_path) 
        workbench_list = [f for f in os.listdir('.') if os.path.isfile(f) and "workbench" in f.lower()]
        print(workbench_list)
        self.hideoutMoveLeft()
        for node in workbench_list:
            if pygui.locateOnScreen(node, confidence=0.75) != None:
                node_loc = pygui.locateOnScreen(node, confidence=0.7)
                node_point = pygui.center(node_loc)
                nodex, nodey = node_point
                pygui.click(x=nodex, y=nodey)
                sleep(1)
                os.chdir(self.item_path) 
                self.reusableBPExitLoop()
                # bpX, bpY = pygui.center(pygui.locateOnScreen("762bp_item_icon.png"))
                # greenX, greenY = pygui.center(pygui.locateOnScreen("GreenGunpowder_item_icon.png"))
                # blueX, blueY = pygui.center(pygui.locateOnScreen("BlueGunpowder_item_icon.png"))  
                if pygui.locateOnScreen("MultitoolReady_item_icon.png", confidence=0.9) != None: 
                    print('MULTI READY')
                    self.clickToFilter(self.item_path, "BlueGunpowder_item_icon.png")
                    print("LICKED")
                    self.buyOnFlea(2)
                    print("eagle check")
                    self.fleaMarketSearch("Gunpowder \"Eagle\"")
                    print("second")
                    self.buyOnFlea(2)
                elif pygui.locateOnScreen("MultitoolNotReady_item_icon.png", confidence=0.9) != None: 
                    print("MULTI NOT READY")
                    self.clickToFilter(self.item_path, "MultitoolNotReady_item_icon.png")
                    self.buyOnFlea(1)
                    self.fleaMarketSearch("Gunpowder \"Kite\"")
                    self.buyOnFlea(2)
                    self.fleaMarketSearch("Gunpowder \"Eagle\"")
                    self.buyOnFlea(2)
                else:
                    print("COULDNT FIND MULTI")
                    return "fail"
                #this is done after all purchases
                pygui.press("esc")
                self.reusableBPExitLoop()
                os.chdir(self.recipes)
                bp_loc = pygui.locateOnScreen("762BPStart_recipe.png")
                if bp_loc != None:
                    pygui.click(pygui.center(bp_loc))
                    sleep(0.1)
                    pygui.press("y")
                else:
                    print("No BP found! or its not ready yet")
                    return "fail"
                
                
        return "Fail"        
        
 