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
        self.icons_path = os.path.join(self.base_path, 'Icons')
        self.submenu_path = os.path.join(self.icons_path, "Submenu_Options")
 
    def runExe(self):
        subprocess.Popen(self.tarkov_path)
        
    def pressPlay(self):
        #Click "play"
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("Play_button.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("Play_button.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
        else:
            print("Error: Tarkov launcher not found on screen")
            return "FATAL"
        
    def checkForButtons(self):
        os.chdir(self.submenu_path)
        i = 0
        while True:
            if pygui.locateOnScreen("mainmenu_block.png", confidence=0.9):
                print("Main menu found")
                return
            if i == 45:
                pygui.click(x=960, y=540)
                continue
            if i > 90:
                print("No buttons found after 90 sec")
                return "FATAL"
            i += 1    
            sleep(1)    
            
    def fullRun(self):
        if self.tarkov_path.lower().endswith("bsglauncher.exe") != True:
            print("Error: Invalid path")
            return 'fail'
        self.runExe()
        sleep(7.5)
        status = self.pressPlay()
        if status == "FATAL":
            return "FATAL"
        main_menu = self.checkForButtons()
        if main_menu == "FATAL":
            return "FATAL"
        return "success"
        
            