# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:33:12 2022

@author: vinch
"""

#subnode test
from Hideout import Hideout
import pyautogui as pygui
import cv2
from time import sleep
import os

while True:
    user = input("y/n\n")
    if user == "y":
        break
sleep(5)

all_paths = ["C:\\Users\\vinch\\Desktop\\SubNodes\\btcComplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\btcIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\boozeIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\boozeComplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\medIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\nutritionIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\medComplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\scavComplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\scavIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\waterComplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\waterIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\workbenchComplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\workbenchIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\generator_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\intelIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\lavIncomplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\nutritionComplete_subnode.png",
             "C:\\Users\\vinch\\Desktop\\SubNodes\\lavComplete_subnode.png"]

my_hideout = Hideout(os.getcwd())

right_nodes = ["med", "nutrition", "booze", "water"]
left_nodes = ["workbench", "intel", "lav", "btc"]
middle_nodes = ["scav", "generator"]
for path in all_paths:
    complete = False
    for node in right_nodes:
        if node in path:
            my_hideout.hideoutMoveRight()
            if pygui.locateCenterOnScreen(path, confidence=0.625) != None:
                sleep(0.1)
                point_x, point_y = pygui.locateCenterOnScreen(path, confidence=0.625)
                pygui.click(point_x, point_y)
                print(path + " node found!")
                complete = True
                sleep(1)
                pygui.press('esc')
                sleep(0.75)
                break
    if complete == False:
        for node in left_nodes:
            if node in path:
                my_hideout.hideoutMoveLeft()
                if pygui.locateCenterOnScreen(path, confidence=0.625) != None:
                    sleep(0.1)
                    point_x, point_y = pygui.locateCenterOnScreen(path, confidence=0.625)
                    pygui.click(point_x, point_y)
                    print(path + " node found!")
                    complete = True
                    sleep(1)
                    pygui.press('esc')
                    sleep(0.75)
                    break
    if complete == False:
        for node in middle_nodes:
            my_hideout.hideoutReset()
            if pygui.locateCenterOnScreen(path, confidence=0.625) != None:
                sleep(0.1)
                point_x, point_y = pygui.locateCenterOnScreen(path, confidence=0.625)
                pygui.click(point_x, point_y)
                print(path + " node found!")
                complete = True
                sleep(1)
                pygui.press('esc')
                sleep(0.75)
                break
    if complete == False:
        print("Error: " + path + " not found on screen!")
        
        
#SUBNODE CONFIDENCE LEVEL: 0.625 (CURRENTLY DONT NEED MID STATUS

def checkForClaimS(self):

    def getAllItems(self):
        #need to somehow stop if hideout doesnt have all nodes
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        
        self.goToHideout()
        
        os.chdir(self.subnodes_path)
        dir_list = [f for f in os.listdir('.') if os.path.isfile(f) and '_subnode' in f]
        right_nodes = ["med", "nutrition", "booze", "water"]
        left_nodes = ["workbench", "intel", "lav", "btc"]
        middle_nodes = ["scav"]
        total_nodes = ["med", "nutrition", "booze", "water","workbench", "intel", "lav", "btc","scav", "generator"]
        scroll_counts = {"med":37, "nutrition":32, "booze":0, "water":0, "workbench":130, "intel":20, "lav":55, "btc":0, "scav":7} 
        claimed_count = 0
        for node in total_nodes:
            node_found = False
            if node in right_nodes:
                self.hideoutMoveRight()
                node_complete_name = node+"Complete_subnode.png"
                node_incomplete_name = node+"Incomplete_subnode.png"
                if pygui.locateCenterOnScreen(node_complete_name, confidence=0.625) != None:
                    point_x, point_y = pygui.locateCenterOnScreen(node_complete_name, confidence=0.625)
                    pygui.click(x=point_x, y=point_y)
                    node_found = True
                    sleep(0.5)
                elif pygui.locateCenterOnScreen(node_incomplete_name, confidence=0.625) != None:
                    point_x, point_y = pygui.locateCenterOnScreen(node_incomplete_name, confidence=0.625)
                    pygui.click(x=point_x, y=point_y)
                    node_found = True
                    sleep(0.5)
            elif node in left_nodes:
                self.hideoutMoveLeft()
                node_complete_name = node+"Complete_subnode.png"
                node_incomplete_name = node+"Incomplete_subnode.png"
                if pygui.locateCenterOnScreen(node_complete_name, confidence=0.625) != None:
                    point_x, point_y = pygui.locateCenterOnScreen(node_complete_name, confidence=0.625)
                    pygui.click(x=point_x, y=point_y)
                    node_found = True
                    sleep(0.5)
                elif pygui.locateCenterOnScreen(node_incomplete_name, confidence=0.625) != None:
                    point_x, point_y = pygui.locateCenterOnScreen(node_incomplete_name, confidence=0.625)
                    pygui.click(x=point_x, y=point_y)
                    node_found = True
                    sleep(0.5)
            elif node in middle_nodes:
                self.hideoutReset()
                node_complete_name = node+"Complete_subnode.png"
                node_incomplete_name = node+"Incomplete_subnode.png"
                if pygui.locateCenterOnScreen(node_complete_name, confidence=0.625) != None:
                    point_x, point_y = pygui.locateCenterOnScreen(node_complete_name, confidence=0.625)
                    pygui.click(x=point_x, y=point_y)
                    node_found = True
                    sleep(0.5)
                elif pygui.locateCenterOnScreen(node_incomplete_name, confidence=0.625) != None:
                    point_x, point_y = pygui.locateCenterOnScreen(node_incomplete_name, confidence=0.625)
                    pygui.click(x=point_x, y=point_y)
                    node_found = True
                    sleep(0.5)
            
            if node_found == True:
                print(node + " identified and clicked")
            else:
                print("Error: Node not found in search..killing")
                return "FATAL"
            
            checker = False
            
            for i in range(scroll_counts[node]):
                pygui.moveTo(x=1410, y=655)
                pygui.scroll(-10)
                status = self.checkForClaim(node)
                if status == None:
                    print("Item claimed for node " + node)
                    claimed_count += 1
                    checker = True
                    break
            
            if checker == True:
                continue
            
            if scroll_counts[node] == 0:
                status = self.checkForClaim(node)
                if status == None:
                    print("Item claimed for node " + node)
                    claimed_count += 1
                    continue
                else:
                    print("Nothing to grab from " + node)
                    continue
                
            print("Nothing to grab from node " + node)
                
        print("Successfully grabbed " + str(claimed_count) + " item(s)")
        