# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 13:31:00 2022

@author: vinch
"""
#<><><><><><><><>
#---------------
#TarkovBotV1
#---------------
#<><><><><><><><>

#Use sentiment to define photo groups (Ready to go, Unable to go etc.)
#THIS IS OG STRAT
 
import pyautogui as pygui
from time import sleep
import random
import cv2
import os
 


class Hideout:
    
    def __init__(self):

        self.base_path = os.getcwd()
        self.photos_path = os.path.join(self.base_path, 'Icons')
        self.blocks_path = os.path.join(self.base_path, 'Blocks')
        self.statuses = ["working_full", "working_empty", "working_half", "incomplete", "na", "locked", "complete"] 
        self.node_names = ["air", "booze", "btc", "generator", "heating", "illumination", "intel", "lav", "library", "med", "nutrition", "rest", "scav", "vents", "water", "workbench"] 
        self.current_statuses = []
        
    def goToHideout(self):
        #Click "Hideout" (Bottom)
        pygui.click(x=201, y=1057)
        #Sleeps 10 so hideout has enough time to load
            #may want to do a while loop that checks every second for a valid button 
        # sleep(10)
        
    def hideoutReset(self): 
        #reset to middle
        pygui.press('enter')
        sleep(0.25)
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
  
    def findStatus(self, node_name):
        #Finds status of node given node_name 
        self.goToHideout()
        os.chdir(self.photos_path) #grab directory contents (specifically files)
        dir_contents = [f for f in os.listdir('.') if os.path.isfile(f)]
        #confirms only files with valid node name accepted 
        chopped_contents = [f for f in dir_contents if node_name.lower() in f.lower()]  
        file_name = " "
 
        for file in chopped_contents: 
            self.hideoutReset()
            sleep(0.3)
            #attempt to locate icon
            node_loc = pygui.locateOnScreen(file, confidence=0.75)
            print(node_loc)
            if node_loc == None: 
                #move left
                self.hideoutMoveLeft()
                #attempt to locate icon
                node_loc = pygui.locateOnScreen(file, confidence=0.75)
                
                if node_loc == None: 
                    #move right
                    self.hideoutMoveRight() 
                    #attempt to locate icon
                    node_loc = pygui.locateOnScreen(file, confidence=0.75) 
                    if node_loc == None:
                        #This means this icon was not found onscreen  
                        continue
                    else:
                        file_name = file
                        break
                else:
                    file_name = file
                    break
            else:        
                file_name = file
                break
            
        if file_name == " ": 
            return None 
        
        for status in self.statuses:
            # cut off .png
            print('b') 
            file_name_chopped = file_name[:-4]
                                          
            if file_name_chopped.lower().endswith(status): 
                return status
    
    def findAllStatuses(self):
 
        for node_name in self.node_names:
            status = self.findStatus(node_name) 
            self.current_statuses.append((node_name, status))
            print((node_name, status)) 
            sleep(1) 
            
        return self.current_statuses
   



