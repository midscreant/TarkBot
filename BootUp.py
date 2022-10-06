# -*- coding: utf-8 -*-

#BOOTER

import subprocess
import os
import cv2
import pyautogui as pygui
from time import sleep

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
            print("ERROR: Tarkov launcher not found on screen. Ending run...")
            return "FATAL"
        
    def checkForButtons(self):
        os.chdir(self.submenu_path)
        i = 0
        while True:
            if pygui.locateOnScreen("mainmenu_block.png", confidence=0.9):
                print("SUCCESSFULLY COMPLETED INITIAL MAIN MENU CHECK")
                return
            if i == 45:
                pygui.click(x=960, y=540)
                continue
            if i > 90:
                print("ERROR: No buttons found after 90 sec. Ending run...")
                return "FATAL"
            i += 1    
            sleep(1)    
            
    def fullRun(self):
        if self.tarkov_path.lower().endswith("bsglauncher.exe") != True:
            print("ERROR: Invalid path")
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