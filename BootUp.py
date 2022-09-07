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
    
    def __init__(self):
        self.tarkovPath = "C:/Battlestate Games/BsgLauncher/BsgLauncher.exe"
        self.base_path = os.getcwd()
        self.photos_path = os.path.join(self.base_path, 'Icons')
        self.blocks_path = os.path.join(self.base_path, 'Blocks')
 
    def runExe(self):
        #doesnt work
        subprocess.call(self.tarkovPath)
        
    def pressPlay(self):
        #Click "play"
        pygui.click(x=1301, y=805, duration=1) 
        
    def checkForButtons(self):
        #checks if there are eft buttons on screen
        os.chdir(self.blocks_path)
        _exit = False
        i = 0
        while _exit == False:
            if pygui.locateOnScreen("homescreen_block.png", confidence=0.9):
                _exit = True
            if i > 60:
                print("No buttons found after one minute.")
                return "fail"
            i += 1    
            sleep(1)    
            
            