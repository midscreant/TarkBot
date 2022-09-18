# -*- coding: utf-8 -*-

"""
Created on Tue Aug 23 23:22:34 2022

@author: vinch
"""

#Tarkov boot bot

#ASSUMES 1920x1080

import subprocess
from time import sleep
import pyautogui as pygui
import os
import cv2


class BootUp:
    
    def __init__(self, tarkov_path, base_path):
        self.tarkov_path = tarkov_path
        self.base_path = base_path
        self.photos_path = os.path.join(self.base_path, 'Icons')
        self.blocks_path = os.path.join(self.photos_path, "Submenu_Options")
 
    def runExe(self):
        #doesnt work
        subprocess.Popen(self.tarkov_path)
        
    def pressPlay(self):
        #Click "play"
        pygui.click(x=1301, y=805, duration=1) 
        
    def checkForButtons(self):
        #checks if there are eft buttons on screen
        os.chdir(self.blocks_path)
        i = 0
        while True:
            if pygui.locateOnScreen("mainmenu_block.png", confidence=0.9):
                print("Main menu found")
                return
            if i == 60:
                pygui.click(x=960, y=540)
                continue
            if i > 120:
                print("No buttons found after two minutes.")
                return "fail"
            i += 1    
            sleep(1)    
            
    def fullRun(self):
        if self.tarkov_path.lower().endswith("bsglauncher.exe") != True:
            print("Error: Invalid path")
            return 'fail'
        self.runExe()
        sleep(7.5)
        self.pressPlay()
        main_menu = self.checkForButtons()
        if main_menu == "fail":
            return "fail"
        return "success"
        
            