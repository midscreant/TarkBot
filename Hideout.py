# -*- coding: utf-8 -*-

#HIDEOUT

from recipes___ import all_recipes

import cv2
import os 
import pytesseract
import pyautogui as pygui
from PIL import Image
from time import sleep 
 

class Hideout:
    
    def __init__(self, base_path):

        self.base_path = base_path
        #temp path
        self.temp_path = os.path.join(self.base_path, "temp")
        os.chdir(self.base_path)
        if os.path.isdir(self.temp_path) == False:
            os.mkdir(self.temp_path)
        #icons path
        self.icons_path = os.path.join(self.base_path, 'Icons')
        #nodes path
        self.nodes_path = os.path.join(self.icons_path, 'Nodes') 
        #subnodes path
        self.subnodes_path = os.path.join(self.icons_path, 'SubNodes') 
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
        
        #tesseract defs
        self.strip_var = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*)(}{-_=+><\\/?'\";:][.\n "
        self.tools_folder_path = os.path.join(self.base_path, "tools")
        self.tesseract_folder_path = os.path.join(self.tools_folder_path, "tesseract")
        self.tesseract_exe_path = os.path.join(self.tesseract_folder_path, "tesseract")
    
        self.share_folder_path = os.path.join(self.base_path, "share")
        self.tessdata_path = os.path.join(self.share_folder_path, "tessdata")
                
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_exe_path
        self.tessdata_dir_config = '--tessdata-dir "'+self.tessdata_path+'"'
        
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
        os.chdir(self.submenu_path)
        if pygui.locateCenterOnScreen("close_button.png", confidence=0.85) != None:
            point_x, point_y = pygui.locateCenterOnScreen("close_button.png", confidence=0.85)
            pygui.click(x=point_x, y=point_y)
            sleep(0.75)
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
            print("FATAL ERROR: Not on home screen. Ending run...")
            return "FATAL"
        print("---ON MAIN MENU: CONFIRMED")
        sleep(0.3)
        
        
    #<><><><><><><><><><><><><>    
    #Passive Hideout Functions
    #<><><><><><><><><><><><><>
    
    def checkForClaim(self, node_name):
        os.chdir(self.submenu_path)
        dir_list = [f for f in os.listdir('.') if os.path.isfile(f) and '_claim' in f]
        for claim in dir_list:
            if pygui.locateCenterOnScreen(claim, confidence=0.75) != None:
                if node_name != "scav":
                    point_x, point_y = pygui.locateCenterOnScreen(claim,confidence=0.75)
                    pygui.click(x=point_x, y=point_y)
                    if pygui.locateOnScreen("NoSpaceHideout_status.png", confidence=0.9) != None:
                        print("ERROR: No space in inventory to claim item. Ending run...")
                        #this should definitely kill
                        return "FATAL"
                    print("Item successfully claimed from " + node_name)
                    return
                point_x, point_y = pygui.locateCenterOnScreen(claim,confidence=0.75)
                pygui.click(x=point_x, y=point_y)
                sleep(1)
                if pygui.locateCenterOnScreen("receive_claim.png", confidence=0.75) == None:
                    print("ERROR: No space in inventory to claim scav items. Continuing run")
                    return 'none'
                _point_x, _point_y = pygui.locateCenterOnScreen("receive_claim.png", confidence=0.75)
                pygui.click(x=_point_x, y=_point_y)
                print("Items successfully claimed from the scav case")
                return
            else:
                continue
        return 'none'
    
    def getAllItems(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        
        self.goToHideout()
        
        os.chdir(self.subnodes_path)
        total_nodes = ["med", "nutrition", "booze", "water","workbench", "intel", "lav", "btc", "scav"] 
        scroll_counts = {"med":37, "nutrition":37, "booze":0, "water":0, "workbench":130, "intel":25, "lav":70, "btc":0, "scav":13}
        claimed_count = 0
        for node in total_nodes:
            node_found = self.locateNode(node)
            if node_found != True:
                print("ERROR: Node not found. Ending run...")
                return "FATAL"
            os.chdir(self.submenu_path)
            if (pygui.locateCenterOnScreen("production_status.png", confidence=0.8) != None and node != "water") or (pygui.locateCenterOnScreen("collecting_status.png", confidence=0.8) != None and node != "water"):
                #this means the node is still producing, so nothing to claim
                print(node.capitalize() + " currently running. Nothing to claim")
                print("<--------->")
                continue
            
            checker = False
            
            for i in range(scroll_counts[node]):
                if i%6 == 0:
                    status = self.checkForClaim(node)
                    if status == None:
                        print("<--------->")
                        claimed_count += 1
                        checker = True
                        break
                    if status == "na":
                        break
                    if status == "FATAL":
                        return "FATAL"
                pygui.moveTo(x=1410, y=655)
                pygui.scroll(-10)
            if checker == True:
                continue
            
            if scroll_counts[node] == 0:
                status = self.checkForClaim(node)
                if status == "FATAL":
                    return "FATAL"
                if status == None:
                    print("<--------->")
                    claimed_count += 1
                    continue
                
            print("Nothing to grab from " + node.capitalize())
            print("<--------->")
                
        print("Claim check claimed " + str(claimed_count) + " item(s)")
    
        
    #<><><><><><><><><><><><><>
    #TESSERACT Functions
    #<><><><><><><><><><><><><>
        
    def checkStack(self):
        os.chdir(self.temp_path)
        pygui.screenshot("number_ss.png",region=(825,534,225,23))
        sleep(0.2)
        image_string = pytesseract.image_to_string(Image.open(r'number_ss.png'), config=self.tessdata_dir_config).strip(self.strip_var)
        try:
            os.remove("number_ss.png")
        except:
            print("ERROR: Couldn't delete image. Ending run...")
            return "FATAL"
        if len(image_string) == 0:
            print("ERROR: Null data recovered from OCR. Ending run...")
            return "FATAL"
        try:
            box_value = int(image_string)
            #this is the actual amount written out in stack buy prompt
            return box_value
        except ValueError:
            print("ERROR: Corrupted data recovered from OCR. Ending run...")
            return "FATAL"
            
    def attemptStackPurchase(self, initial_count):
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("stackPartialBuy_status.png", confidence=0.9) == None and pygui.locateOnScreen("alreadyPurchased_status.png", confidence=0.85) == None:
            print("Successfully purchased the full stack")
            return initial_count
        elif pygui.locateOnScreen("stackPartialBuy_status.png", confidence=0.9) != None:
            status = self.checkForNoMoney()
            if status == "FATAL":
                return "FATAL"
            print("Successfully purchased a partial stack")
            os.chdir(self.temp_path)
            pygui.screenshot("partialBlock_ss.png",region=(825,492,327,55))
            sleep(0.2)
            image_string = pytesseract.image_to_string(Image.open(r'partialBlock_ss.png'), config=self.tessdata_dir_config).strip(self.strip_var)
            try:
                os.remove("partialBlock_ss.png")
            except:
                print("ERROR: Couldn't delete image. Ending run...")
                return "FATAL"
            split_list = image_string.split(" ")
            int_list = []
            for item in split_list:
                try:
                    int_value = int(item)
                    int_list.append(int_value)
                except:
                    continue
            if len(int_list) != 2:
                print("ERROR: Not enough numbers found on-screen. Ending run...")
                return "FATAL"
            amount_purchased = int_list[1]
            pygui.press('esc')
            return amount_purchased
        elif pygui.locateOnScreen("alreadyPurchased_status.png", confidence=0.85) != None:
            print("Failed to buy any of the stack. Retrying...")
            return 0
        else:
            print("ERROR: Unknown Fatal Error. Ending run...")
            return "FATAL"
        
        
 
    #<><><><><><><><><><><><><>
    #Active Hideout Functions
    #<><><><><><><><><><><><><>

    def bottomFlea(self):
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("fleaMarket_button.png", confidence=0.9) == None:
            print("ERROR: Flea market button not on screen. Ending run...")
            return "FATAL"
        
        point_x, point_y = pygui.locateCenterOnScreen("fleaMarket_button.png", confidence=0.9)
        pygui.click(x=point_x, y=point_y)
        sleep(1)
        if pygui.locateOnScreen("fleaMarketConfirm_status.png", confidence=0.9) == None:
            print("ERROR: Top flea market button not on screen")
            #this is a reset click
            pygui.click(x=1395, y=543)
            sleep(0.25)
            point_x, point_y = pygui.locateCenterOnScreen("fleaMarket_button.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(1)
            if pygui.locateOnScreen("fleaMarketConfirm_status.png", confidence=0.9) == None:
                print("ERROR: Top flea market button not on screen. Ending run...")
                return "FATAL"
        print("---Bottom flea successfully pressed")
    
    def checkForNoMoney(self):
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("NotEnoughMoney_status.png", confidence=0.9) == None:
            return
        print("ERROR: Not enough money to continue to run bot. Ending run...")
        return "FATAL"
    
    
    def startRecipe(self, item_pic_name, node_name=None):
        if type(item_pic_name) == tuple:
            if node_name != None:
                print("ERROR: Can't submit both tuple and node name")
                return 'fail' 
            item_pic_name_list = item_pic_name
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
            print("ERROR: Invalid node name")
            return 'fail'
        item_loc = None
        try:
            pic_int = int(item_pic_name)
            item_loc = pygui.locateOnScreen(item_pic_name + "_status.png", confidence=0.85) 
        except:
            item_loc = pygui.locateOnScreen(item_pic_name + "_recipe.png", confidence=0.85) 
        if item_loc != None:
            item_left_x = item_loc.left
            item_width = item_loc.width 
            item_x, item_y = pygui.center(item_loc) 
            #shift 72 pixels right to click start button
            if node_name == "scav":
                pygui.click(x=item_left_x + 330, y=item_y)
            else:
                pygui.click(x=item_left_x + item_width + 72, y=item_y)
            sleep(0.25)
            pygui.press("y")
            sleep(2)
            os.chdir(self.submenu_path)
            if pygui.locateOnScreen("production_status.png", confidence=0.9) != None or pygui.locateOnScreen("collecting_status.png", confidence=0.9) != None:
                print(item_pic_name + " recipe successfully started") 
                return
            else:
                print("Unable to start " + item_pic_name + " recipe") 
                return "fail"
        else:
            print("ERROR: No " + item_pic_name + " recipe found") 
            return "fail" 
    
    
    def buyAid(self, item_name, count=None, offset=None):
        #assumes you are on flea and at correct item, as does parent  
        #offset is an int for jumping down a certain count of purchase buttons
        
        if item_name.lower() == "water filter" or "fuel tank" in item_name.lower():
            if count == None or count==0:
                #For one filter/tank
                status = self.buyFullContainer()
                if status == "buy_fail":
                    return "buy_fail"
                print("Purchased all containers (full)")
                return
            _i = 0
            while True:
                #For multiple
                if _i == count:
                    print("Purchased all containers (full)")
                    break
                
                status = self.buyFullContainer()
                if status == "buy_fail":
                    return "buy_fail"
                _i += 1
            
        elif count != None: 
            if offset == None or offset == 0:
                pygui.click(x=1761, y=179)
                sleep(0.75)
                pygui.doubleClick(x=1035, y=490)
                sleep(0.5)
                pygui.write(str(count), interval=0.075)
                sleep(0.5)
                status = self.checkStack()
                if status == "FATAL":
                    return "FATAL"
                if count == status:
                    print("Attempting full stack purchase")
                else:
                    print("Attempting purchase of " + str(status) + " out of " + str(count))
                pygui.press("y")
                sleep(0.75)
                _status = self.attemptStackPurchase(status)
                revised_count = None
                if _status == "FATAL":
                    return "FATAL"
                elif count <= status:
                    #successful full stack purchase
                    sleep(0.75)
                    return
                else:
                    revised_count = count - _status
                    if revised_count <= 0:
                        print("All items successfully purchased")
                        return
                self.buyAid(item_name, revised_count, offset)
                
            else:    
                pixel_offset = 72 * offset
                pygui.click(x=1762, y=179+pixel_offset)
                sleep(0.75)
                pygui.doubleClick(x=1035, y=490)
                sleep(0.5)
                pygui.write(str(count), interval=0.075)
                sleep(0.5)
                status = self.checkStack()
                if status == "FATAL":
                    return "FATAL"
                if count == status:
                    print("Attempting full stack purchase")
                else:
                    print("Attempting purchase of " + str(status) + " out of " + str(count))
                pygui.press("y")
                sleep(0.75)
                _status = self.attemptStackPurchase(status)
                revised_count = None
                if _status == "FATAL":
                    return "FATAL"
                elif count >= status:
                    sleep(0.75)
                    return
                else:
                    revised_count = count - _status
                    

                self.buyAid(item_name, revised_count, offset)
                
        elif offset == None or offset == 0:
            pygui.click(x=1761, y=179)
            sleep(0.5)
            pygui.press("y")
            sleep(0.75)
            
        else:
            pixel_offset = 72 * offset
            pygui.click(x=1762, y=179+pixel_offset)
            sleep(0.5)
            pygui.press("y")
            sleep(0.75)
            
        status = self.checkForNoMoney()
        if status == "FATAL":
            return "FATAL"
        
            
    def buyFullContainer(self):
        
        top = None
        left = None
        width = None
        height = None
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("100100_status.png", confidence=0.9) != None:
            left, top, width, height = pygui.locateOnScreen("100100_status.png", confidence=0.9)
        elif pygui.locateOnScreen("6060_status.png", confidence=0.9) != None:
            left, top, width, height = pygui.locateOnScreen("6060_status.png", confidence=0.9)
        else:
            while True:
                _i = 0
                show_more = False
                
                if pygui.locateCenterOnScreen("FleaRefresh_button.png",confidence=0.9) != None:
                    point_x, point_y = pygui.locateCenterOnScreen("FleaRefresh_button.png",confidence=0.9)
                    pygui.click(x=point_x, y=point_y)
                else:
                    print("ERROR: No refresh button found")
                    
                while True:
                    if _i%2 == 0:
                        if pygui.locateOnScreen("100100_status.png", confidence=0.9) != None:
                            left, top, width, height = pygui.locateOnScreen("100100_status", confidence=0.9)
                            break
                        elif pygui.locateOnScreen("6060_status.png", confidence=0.9) != None:
                            left, top, width, height = pygui.locateOnScreen("6060_status.png", confidence=0.9)
                            break
                            
                    if pygui.locateCenterOnScreen("ShowMore_button.png", confidence=0.9) != None and show_more == False:
                        point_x, point_y = pygui.locateCenterOnScreen("ShowMore_button.png", confidence=0.9)
                        pygui.click(x=point_x, y=point_y)
                        show_more = True
                        sleep(0.25)
                    
                    elif pygui.locateCenterOnScreen("ShowMore_button.png", confidence=0.9) != None and show_more == True:
                        print("ERROR: Went to new page but still no charged items. Buy Fail")
                        return "buy_fail"
                        
                    pygui.moveTo(x=1410, y=655) 
                    pygui.scroll(-10)
                    _i += 1
                
        pos_x = left + 720
        
        pygui.click(x=pos_x, y=top)
        sleep(0.5)
        pygui.press('y')
        sleep(0.75)
        if pygui.locateOnScreen("PurchaseComplete_option.png", confidence=0.9) != None:
            return
        print("ERROR: Purchase success not found. Buy Fail")
        return "buy_fail"
        
       
        
    def buyOnFlea(self, count, item_name, offset=None):  
        _index = 0
        _z = 0 
        _exit = 0 
        if count > 5 and count <= 10:
            _exit = 12
        else:
            _exit = 8 
        os.chdir(self.submenu_path)
        while _index < count and _z < _exit: 
            if _z % 3 == 0:
                if pygui.locateCenterOnScreen("FleaRefresh_button.png",confidence=0.9) != None:
                    point_x, point_y = pygui.locateCenterOnScreen("FleaRefresh_button.png",confidence=0.9)
                    pygui.click(x=point_x, y=point_y)
                    sleep(1)
                else:
                    print("ERROR: No refresh button found")
            if count > 3:
                #moves to stack purchase
                status = self.buyAid(item_name, count, offset)
                if status == "buy_fail":
                    return "buy_fail"
                elif status == "FATAL":
                    return "FATAL"
            else:
                status = self.buyAid(item_name, offset=offset) 
                if status == "buy_fail":
                    return "buy_fail"
                elif status == "FATAL":
                    return "FATAL"
            if pygui.locateOnScreen("PurchaseComplete_option.png", confidence=0.7) != None and count <= 3:
                _index += 1
                print(item_name+" purchased")
                sleep(2.75)
            elif pygui.locateOnScreen("PurchaseComplete_option.png", confidence=0.7) != None:
                print(item_name+" purchased")
                sleep(2.75)
                break
            else:
                print("Purchase failed, retrying")
                _z += 1
        if _z == _exit:
            if _index == 0: 
                print("All purchases failed")
            else:
                end_count = count - _index
                print(str(_index) + " successful purchases. " + str(end_count) + " failed")
            sleep(0.25)
            return "fail"
        else:
            sleep(0.25)
            print("All "  + str(count) + " " + item_name + "(s) successfully purchased")       
 
    
    def fleaMarketSearch(self, item_name):
        #assumes you are already on the flea
        #assumes you already have a specific item selected 
        pygui.click(x=258, y=121)
        pygui.write(item_name, interval=0.2525)
        sleep(1)
        #Click "x"s 
        os.chdir(self.submenu_path)
        all_points = list(pygui.locateAllOnScreen("Exit_Option.png", confidence=0.9))
        if len(all_points) == 3: 
            point_1x, point_1y  = pygui.center(all_points[0]) 
            pygui.click(x=point_1x, y=point_1y)
            sleep(0.3)
            refreshed_points = list(pygui.locateAllOnScreen("Exit_Option.png", confidence=0.9))
            point_2x, point_2y = pygui.center(refreshed_points[1]) 
            pygui.click(x=point_2x, y=point_2y)
            sleep(1.25)
        else:
            sleep(1)
        pygui.click(x=1501, y=27)
        sleep(0.25)
        #clicks item name on left
        if item_name.lower() == 'pliers' or item_name.lower() == 'screwdriver':
            #these items were problomatic so added extra check. position 3
            pygui.click(x=155, y=234)
        elif 'm856' in item_name.lower() or 'm855' in item_name.lower() or "rechargeable" in item_name.lower() or "weapon parts" in item_name.lower():
            #these too. position 2
            pygui.click(x=218, y=196)
        else:    
            pygui.click(x=187, y=164)
        sleep(1)
        
    def checkIfAvailable(self):
        #ASSUMES YOU ARE ON ITEM'S FLEA SCREEN
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("purchase_button.png", confidence=0.9) != None:
            return
        elif pygui.locateOnScreen("outOfStock_status.png", confidence=0.9) != None:
            print("ERROR: Item is out of stock. Skipping recipe for now")
            return "OOS"
        elif pygui.locateOnScreen("NoOffers_status.png", confidence=0.9) != None:
            print("ERROR: Item is either never sold or not currently in stock. Removing recipe from your list")
            return "fail"
        elif pygui.locateOnScreen("locked_status.png", confidence=0.9) != None:
            print("ERROR: Item is locked. Either trader level inadequate, or quest not completed. Removing recipe from your list")
            return "fail"
        print("ERROR: No statuses found. Ending run...")
        return "FATAL"
        
        
    def checkAndBuyRecipe(self, recipe):
        #EXPECTS YOU TO HAVE ALREADY MOVED TO IT ON SCREEN 
        #recipe {"ingredient_1":count, ...} 
        print("<><><><><><><><><><>")
        print("Shopping list ready")
        print("---------------------")
        print(recipe)
        print("<><><><><><><><><><>")
        pygui.press('esc')
        status = self.bottomFlea()
        if status == "FATAL":
            return "FATAL"
        sleep(1)
        if type(recipe) != dict:
            #this means scav
            self.fleaMarketSearch(recipe)
            status = self.checkIfAvailable()
            if status == "fail":
                return "buy_fail"
            elif status == "OOS":
                return "OOS"
            elif status == "FATAL":
                return "FATAL"
            status = self.buyOnFlea(1, recipe)
            if status == "fail":
                return "fail"
            elif status == "buy_fail":
                return "buy_fail"
            elif status == "FATAL":
                return "FATAL"
            return
        for name, count in list(recipe.items()):
            _name = name
            if name.endswith("-_-"):
                _name = name[:-3]
            
            self.fleaMarketSearch(_name)
            status = self.checkIfAvailable()
            if status == "fail":
                return "buy_fail"
            elif status == "OOS":
                return "OOS"
            elif status == "FATAL":
                return "FATAL"
            status = self.buyOnFlea(count, _name)      
            if status == "fail":
                return "fail"
            elif status == "buy_fail":
                return "buy_fail"
            elif status == "FATAL":
                return "FATAL"
            sleep(1)    
     
        
    def reusableExitLoop(self, item_name, node_name):
        _i = 0
        recipe_tuple, recipe_pic_name = self.findRecipe(item_name, node_name)
        _exit_count = 0
        if node_name == "med":
            _exit_count = 37
            os.chdir(self.medstation_recipes_path)
        elif node_name == "intel":
            _exit_count = 25
            os.chdir(self.intel_recipes_path)
        elif node_name == "nutrition":
            _exit_count = 37
            os.chdir(self.nutrition_recipes_path)
        elif node_name == "workbench":
            _exit_count = 130
            os.chdir(self.workbench_recipes_path)
        elif node_name == "scav":
            _exit_count = 13
            os.chdir(self.scav_recipes_path)
        elif node_name == "lav":
            _exit_count = 70
            os.chdir(self.lavatory_recipes_path)
        else:
            print("ERROR: Invalid node name passed")
            return 'fail'
        sleep(0.75)
        while True: 
            if _i%6 == 0:
                sleep(0.25)
                if pygui.locateOnScreen(recipe_pic_name + "_recipe.png", confidence=0.85) != None: 
                    break
            if _i > _exit_count:
                print("ERROR: No item found after " + str(_exit_count) + " attempts")
                return 'fail'
            _i += 1
            pygui.moveTo(x=1410, y=655) 
            pygui.scroll(-10)
 
    
    def locateNode(self, node_name):
        if type(node_name) == tuple:
            node_name = str(node_name[0])
        self.goToHideout()
        right_nodes = [ "med", "nutrition", "booze", "water"]
        left_nodes = ["workbench", "intel", "lav", "btc"]
        middle_nodes = ["generator", "scav"]
        os.chdir(self.subnodes_path)
        file_list = [f for f in os.listdir('.') if os.path.isfile(f) and node_name in f.lower()]
        if node_name in right_nodes:
            self.hideoutMoveRight()
        elif node_name in left_nodes:
            self.hideoutMoveLeft()
        else:
            self.hideoutReset()
        os.chdir(self.subnodes_path)
        for file in file_list:
            if pygui.locateOnScreen(file, confidence=0.55) != None:
                node_x, node_y = pygui.locateCenterOnScreen(file, confidence=0.55)
                pygui.click(x=node_x, y=node_y)
                print(node_name.capitalize() + " found and clicked")
                sleep(1)
                return True
        print("ERROR: " + node_name.capitalize() + " not found. Node location failure")
        return "fail"
    
    
    def findRecipe(self, recipe_name, node_name):
        #returns tuple (recipe_dict, recipe_pic_name) or (recipe_tuple, recipe_pic_name)
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
        else:
            print("ERROR: Invalid node name")
            return "fail"
        
        for name, value in list(dir_1.items()): 
            if name == recipe_name:
                recipe_pic_name = value
                break
        if recipe_pic_name == " ":
            print("ERROR: No recipe pic name grabbed") 
            return 'fail'
        for name, value in list(dir_2.items()):
            if name == recipe_name: 
                return ((name, value), recipe_pic_name)
        print("ERROR: No recipe for " + recipe_name + " found") 
        return 'fail'
    
       
    def checkIngredientStatus(self, recipe_tuple, recipe_pic_name, node_name):
        #assumes you are in node
        recipe_name, recipe_value = recipe_tuple
        ingredient_count = len(recipe_value.keys())
        status = self.reusableExitLoop(recipe_name, node_name) 
        if status == "fail":
            print("ERROR: Buying full list")
            return "fail"
        status = self.startRecipe(recipe_pic_name, node_name)
        if status != "fail":
            print(recipe_name + " recipe successfully started")
            return
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
            print("ERROR: Invalid node name")
            return 'fail' 
        if pygui.locateOnScreen(recipe_pic_name + "_recipe.png", confidence=0.85) == None:
            print("ERROR: Unknown recipe error. Ending run...")
            return "FATAL"
        sleep(1)
        _left, _top, _width, _height = pygui.locateOnScreen(recipe_pic_name + "_recipe.png", confidence=0.85)
        numbers_bottom = _top + 94
        check_bottom = numbers_bottom + 23
        os.chdir(self.submenu_path)
        raw_checks = list(pygui.locateAllOnScreen("Ready_option.png", confidence=0.95))
        raw_xs = list(pygui.locateAllOnScreen("NotReady_option.png", confidence=0.95))
        _dict = {}
        _i = 0
        for check in raw_checks:
            _left, _top, _width, _height = check
            if _top <= check_bottom + 3 and _top >= numbers_bottom - 3:
                #this means its at valid coords
                key = str(_i)
                _dict[key] = ("check", check)
                _i += 1
        for x in raw_xs:
            _left, _top, _width, _height = x
            if _top <= check_bottom + 3 and _top >= numbers_bottom - 3:
                key = str(_i)
                _dict[key] = ("x", x)
                _i += 1
                
        final_list = []
        for key, value in list(_dict.items()):
            value_name, value_tuple = value
            if value_tuple.left not in final_list:
                final_list.append(value_tuple.left)
            
        final_list.sort()
        #list of top properties of locations ordered smallest X to largest X
        final_dict = {}
        _i = 0
        for coord in final_list:
            for key, value in list(_dict.items()):
                value_name, value_tuple = value
                if value_tuple.left == coord:
                    final_dict[str(_i)] = value_name
                    _i += 1
                    break
                
        if ingredient_count != len(final_dict.keys()):
            print("ERROR: Unable to properly make shopping list. Buying full list")
            return "fail"
        print('Final Recipe: ' + str(final_dict))            
        return final_dict
        #returns dict
            #{"position_key 0":"check", "position_key 1":"x", ...}
        
        
        
   
    def makeRecipe(self, recipe_name, node_name):
        final_recipe_name = recipe_name
        while True:
            if type(final_recipe_name) == str:
                break 
            if type(final_recipe_name) == None:
                print("ERROR: None type not valid recipe")
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
                print("ERROR: No recipe name found after tuple dive")
                return 'fail'
 
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        node_located = self.locateNode(node_name) 
        if node_located == True:   
            sleep(0.5)
            os.chdir(self.submenu_path)
            if pygui.locateCenterOnScreen("production_status.png", confidence=0.8) != None:
                #this means the node is still producing, so nothing to claim
                print(node_name + " currently running. Cannot run recipe")
                return
        if node_name == "scav":
            scav_recipe_name, scav_pic_name = self.findRecipe(recipe_name, node_name)
            status = self.startRecipe(scav_pic_name, node_name)
            if status != "fail":
                return
            if scav_pic_name != "25" and scav_pic_name != "150" and scav_pic_name != "950":
                status = self.checkAndBuyRecipe(scav_recipe_name)
                if status == "fail":
                    return "fail"
                elif status == "buy_fail":
                    return "buy_fail"
                elif status == "FATAL":
                    return "FATAL"
            self.goToHideout()
            _node_located = self.locateNode(node_name)
            if _node_located == True:
                self.reusableExitLoop(scav_recipe_name, node_name)
                self.startRecipe(scav_pic_name, node_name)
                pygui.press("esc")
            else:
                pygui.press("esc")
                return "fail"   
        else:
            recipe_tuple, recipe_pic_name = self.findRecipe(final_recipe_name, node_name)
            _recipe_name, recipe_value = recipe_tuple 
            editable_dict = recipe_value
            ingredient_dict = self.checkIngredientStatus(recipe_tuple, recipe_pic_name, node_name)
            if ingredient_dict == "FATAL":
                return "FATAL"
            elif ingredient_dict == None:
                return
            elif type(ingredient_dict) == dict:
                keys = list(recipe_value.keys())
                for key, value in list(ingredient_dict.items()):
                    if value == "x":
                        continue
                    print(keys)
                    for _key in keys:
                        if int(key) == keys.index(_key):
                            editable_dict.pop(_key)
                            break
            else:
                print("ERROR: Buying full list")
                
            status = self.checkAndBuyRecipe(editable_dict)  
            if status == "fail":
                return "fail"
            elif status == "buy_fail":
                return "buy_fail"
            elif status == "FATAL":
                return "FATAL"
            self.goToHideout()
            _node_located = self.locateNode(node_name)
            if _node_located == True:
                self.reusableExitLoop(recipe_name, node_name)
                self.startRecipe(recipe_pic_name, node_name)
                pygui.press("esc")
            else:
                pygui.press("esc")
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
            print("ERROR: Failed to sort stash")
            return "fail"
        else:
            print("Inventory successfully sorted")
 
           
      
    def boozeChecker(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout() 
        self.locateNode('booze')
        os.chdir(self.submenu_path) 
        if pygui.locateOnScreen("production_status.png", confidence=0.9) != None:
            print("Moonshine currently being produced. Cannot run")
            pygui.press("esc")
            return
        superwater_count = 0
        if pygui.locateOnScreen("0-1Status.png", confidence=0.9) != None:
            superwater_count = 1  
        sugar_count = 0
        if pygui.locateOnScreen("0-2Status.png", confidence=0.9) != None:
            sugar_count = 2
        elif pygui.locateOnScreen("1-2Status.png", confidence=0.9) != None:    
            sugar_count = 1 
        if superwater_count > 0:
            status = self.bottomFlea()
            if status == "FATAL":
                return "FATAL"
            self.fleaMarketSearch("Canister with purified water")
            self.buyOnFlea(1, "Canister with purified water")
            sleep(0.25)           
        if sugar_count > 0:
            self.goToHideout()
            status = self.bottomFlea()
            if status == "FATAL":
                return "FATAL"
            self.fleaMarketSearch("Pack of sugar")
            self.buyOnFlea(sugar_count, "Pack of sugar", 3)
            sleep(0.25)  
        self.locateNode('booze') 
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("start_status.png", confidence=0.9) == None:
            print("ERROR: No start found")
            pygui.press("esc")
            return "fail"
        start_x, start_y = pygui.locateCenterOnScreen("start_status.png", confidence=0.9)
        pygui.click(x=start_x, y=start_y)
        sleep(0.25)
        pygui.press('y')
        print('Successfully began moonshine production') 
        sleep(0.25)
        pygui.press("esc")
    
    
    def btcChecker(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout()
        self.locateNode('btc')
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("GetItemsStatus.png", confidence=0.9) != None:
            status_x, status_y = pygui.locateCenterOnScreen("GetItemsStatus.png", confidence=0.9)
            pygui.click(x=status_x, y=status_y)
            print("Bitcoins claimed")
            pygui.press("esc")
            return
        print('No bitcoins to be claimed')
        pygui.press("esc")
        

    def generatorChecker(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout()
        #Checks if generator has enough fuel (2+ tanks), adds more if not. Buys fuel from jaeger if need be
        #generator images in submenu, _gene
        self.locateNode('generator')
        os.chdir(self.submenu_path) 
        
        #sub-process to check for empty fuel containers
        removed_count = 0
        big_fuel = list(pygui.locateAllOnScreen("BigFuel_loaded.png", confidence=0.9))
        small_fuel = list(pygui.locateAllOnScreen("SmallFuel_loaded.png", confidence=0.9))
        if big_fuel != None or small_fuel != None:
            count = 0
            if type(big_fuel) != None:
                count += len(big_fuel)
            if type(small_fuel) != None:
                count += len(small_fuel)
            if count >= 2:
                no_fuel = list(pygui.locateAllOnScreen("NoFuelSub_status.png", confidence=0.9))
                _count = 0
                if no_fuel != None:
                    _count = len(no_fuel)
                if count - _count >= 2:
                    print(count)
                    print(_count)
                    print("Enough fuel already loaded. Skipping")
                    return
        while True:
            if pygui.locateOnScreen("SmallNoFuel_gene.png", confidence=0.925) != None:
                _left, _top, _width, _height = pygui.locateOnScreen("SmallNoFuel_gene.png", confidence=0.925)
                x_coord = _left + (_width - 7)
                y_coord = _top - 15
                pygui.click(x=x_coord, y=y_coord)
                sleep(0.2)
                point_x, point_y = pygui.locateCenterOnScreen("none_gene.png", confidence=0.9)
                pygui.click(x=point_x, y=point_y)
                sleep(0.5)
                if pygui.locateCenterOnScreen("none_gene.png", confidence=0.9) != None:
                    print("ERROR: Didn't remove fuel")
                    continue
                print("Empty small fuel removed")
                removed_count += 1
            elif pygui.locateOnScreen("BigNoFuel_gene.png", confidence=0.925) != None:
                _left, _top, _width, _height = pygui.locateOnScreen("BigNoFuel_gene.png", confidence=0.925)
                x_coord = _left + (_width - 7)
                y_coord = _top - 15
                pygui.click(x=x_coord, y=y_coord)
                sleep(0.2)
                point_x, point_y = pygui.locateCenterOnScreen("none_gene.png", confidence=0.9)
                pygui.click(x=point_x, y=point_y)
                sleep(0.5)
                if pygui.locateCenterOnScreen("none_gene.png", confidence=0.9) != None:
                    print("ERROR: Didn't remove fuel")
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
            sleep(1)
            scroll_count = 0
            os.chdir(self.submenu_path)
            if pygui.locateOnScreen("sell_button.png", confidence=0.9) == None:
                print("ERROR: NO SELL BUTTON FOUND IN JAEGER")
                return "FATAL"
            point_x, point_y = pygui.locateCenterOnScreen("sell_button.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
            sleep(0.5)
            for i in range(removed_count):
                pygui.moveTo(x=1621, y=587)
                while True:
                    if scroll_count > 125:
                        print("ERROR: Wasn't able to find all of the fuel")
                        break
                    if pygui.locateCenterOnScreen("SmallFuelEmptySale_gene.png", confidence=0.925) != None:
                        point_x, point_y =  pygui.locateCenterOnScreen("SmallFuelEmptySale_gene.png", confidence=0.925)
                        with pygui.hold("ctrl"):
                            pygui.click(x=point_x - 10, y=point_y - 20)
                        break
                    elif pygui.locateCenterOnScreen("BigFuelEmptySale_gene.png", confidence=0.925) != None:
                        point_x, point_y =  pygui.locateCenterOnScreen("BigFuelEmptySale_gene.png", confidence=0.925)
                        with pygui.hold("ctrl"):
                            pygui.click(x=point_x - 10, y=point_y - 20)
                        break
                    pygui.scroll(-10)
                    scroll_count += 1
            if pygui.locateCenterOnScreen("deal_claim.png", confidence=0.925) != None:
                point_x, point_y = pygui.locateCenterOnScreen("deal_claim.png", confidence=0.925)
                pygui.click(point_x, point_y)
            else:
                print("ERROR: No deal to be claimed. Fuel sale failed")
            if self.goToMainMenu() == "FATAL":
                return "FATAL"
            self.goToHideout() 
            self.locateNode('generator')
        
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("noFuel_gene.png", confidence=0.9) != None:
            _left, _top, _width, _height = pygui.locateOnScreen("NoFuel_gene.png", confidence=0.9)
            point_x = _left + _width - 5
            point_y = _top + _height/2
            pygui.click(x=point_x, y=point_y)
        else:
            print("ERROR: Can't find fuel load button")
            return "fail"
        
        if pygui.locateOnScreen("BigFuelLoader_gene.png", confidence=0.9) != None:
            fuel_loc_x, fuel_loc_y = pygui.locateCenterOnScreen("BigFuelFull_gene.png", confidence=0.9)
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Large Fuel Loaded")
            pygui.press("esc") 
            return
        elif pygui.locateOnScreen("SmallFuelLoader_gene.png", confidence=0.9) != None:
            fuel_loc_x, fuel_loc_y = pygui.locateCenterOnScreen("SmallFuelFull_gene.png", confidence=0.9)
            pygui.click(x=fuel_loc_x, y=fuel_loc_y)
            print("Small Fuel Loaded") 
            pygui.press("esc")
            return
        else:
            print("No fuel to load found")
            #this is a reset click
            pygui.click(x=1395, y=543)
            sleep(0.25)
            status = self.bottomFlea()
            if status == "FATAL":
                return "FATAL"
            self.fleaMarketSearch("Metal Fuel Tank")
            
            fuel_loc = pygui.locateOnScreen("JaegerFuelPrice_gene.png", confidence=0.9)
            fuel_point_y = fuel_loc.top + (fuel_loc.height/2)
            fuel_left_x = fuel_loc.left 
            purchase_loc_x = fuel_left_x + fuel_loc.width + 275
            #specifically buying jaeger's offer. will only work if its visible on page 1
            pygui.click(x=purchase_loc_x, y=fuel_point_y)
            sleep(0.25)
            pygui.press('y') 
            print("Large Fuel Successfully Purchased")
            sleep(1)
            self.locateNode('generator')
            os.chdir(self.submenu_path)
            if pygui.locateOnScreen("noFuel_gene.png", confidence=0.9) != None:
                _left, _top, _width, _height = pygui.locateOnScreen("NoFuel_gene.png", confidence=0.9)
                point_x = _left + _width - 5
                point_y = _top + _height/2
                pygui.click(x=point_x, y=point_y)
            else:
                print("ERROR: Can't find fuel load button")
                return "fail"
            if pygui.locateCenterOnScreen("BigFuelFull_gene.png", confidence=0.9) == None:
                print("ERROR: Jaeger was sold out of fuel. No more fuel to load")
                return
            fuel_loc_x, fuel_loc_y = pygui.locateCenterOnScreen("BigFuelFull_gene.png", confidence=0.9)
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
        sleep(0.5)
        os.chdir(self.submenu_path)
        #if there's already a filter loaded, function ends
        if pygui.locateOnScreen("Water_gene.png", confidence=0.9) != None:
            print("Water filter currently loaded and running")
            pygui.press("esc")
            return
        if pygui.locateOnScreen("geneBar_button.png", confidence=0.9) != None:
            point_x, point_y = pygui.locateCenterOnScreen("geneBar_button.png", confidence=0.9)
            pygui.click(x=point_x, y=point_y)
        else:
            print("ERROR: Can't find fuel load button")
            return "fail"
        #if there's no water filters ready to be loaded, buy one on market
        if pygui.locateOnScreen("NoFuelLoader_gene.png", confidence=0.9) != None:
            print("No spare water filters. Buying one from market")
            sleep(0.5)
            status = self.bottomFlea()
            if status == "FATAL":
                return "FATAL"
            self.fleaMarketSearch("Water Filter")
            self.buyOnFlea(1, "Water Filter") 
            if self.goToMainMenu() == "FATAL":
                return "FATAL"
            self.locateNode('water')
            os.chdir(self.submenu_path)
            if pygui.locateOnScreen("geneBar_button.png", confidence=0.9) != None:
                point_x, point_y = pygui.locateCenterOnScreen("geneBar_button.png", confidence=0.9)
                pygui.click(x=point_x, y=point_y)
            else:
                print("ERROR: Can't find fuel load button")
                return "fail"
            if pygui.locateOnScreen("WaterLoader_gene.png", confidence=0.9) == None:
                print("ERROR: Water func unknown failure")
                pygui.press("esc")
                return "fail"
            _water_x, _water_y = pygui.locateCenterOnScreen("Water_gene.png", confidence=0.9)
            pygui.click(x=_water_x, y=_water_y)
            print("Water filter from flea successfully added")
            sleep(0.25)
            pygui.press("esc")
        elif pygui.locateOnScreen("Water_gene.png", confidence=0.9) != None:
           _water_x, _water_y = pygui.locateCenterOnScreen("Water_gene.png", confidence=0.9)
           pygui.click(x=_water_x, y=_water_y)
           print("Water filter from inv successfully added")
           sleep(0.25)
           pygui.press("esc")
           
           
    def gcardBuyAndAdd(self, count=1):
        #Wrote this but never used it. May use when mobile support added
        #buys a graphics card and adds it to btc farm 
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout()  
        status = self.bottomFlea()
        if status == "FATAL":
            return "FATAL"
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
                print("Scav case started with " + item)
                return
            if item == "MOON" or item == "INTEL":   
                status = self.bottomFlea()
                if status == "FATAL":
                    return "FATAL"
                self.fleaMarketSearch(item_full_name)
                self.buyOnFlea(1, item_full_name)
                self.locateNode("scav")
                self.startRecipe(item, "scav")
                pygui.press("esc")
                return
            else:
                print("ERROR: Not enough roubles to run " + item_full_name + " scav case")
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
            print("ERROR. No messenger button found. Flea claim failed")
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
                     print("No space to claim items. Fatal ERROR")
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
                    print("ERROR: No Acceptance found. Ending run...")
                    return "FATAL"
            else:
                print("ERROR: 2nd receive button not found. Ending run...")
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
            print("ERROR: Ragman not found. Flea claim failed")
            return "fail"
        
        status = self.checkReceive()
        if status == "fail":
            print("No flea items to claim")
        elif status == "FATAL":
            print("ERROR: Flea claim error. Ending run...")
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
            print("ERROR: Prapor not found. Flea claim failed")
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
            print("ERROR: Therapist not found. Flea claim failed")
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
        
    def checkForNoFuel(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout()
        self.locateNode("generator")
        sleep(0.5)
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("NoFuel_status.png", confidence=0.9) == None:
            pygui.press('esc')
            return
        print("ERROR: No fuel in generator post-generator check. Ending run...")
        return "FATAL"
    
    def geneOnCheck(self):
        if self.goToMainMenu() == "FATAL":
            return "FATAL"
        self.goToHideout()
        os.chdir(self.submenu_path)
        if pygui.locateOnScreen("GeneOff_status.png", confidence=0.9) == None:
            print("Generator already running")
            return
        point_x, point_y = pygui.locateCenterOnScreen("GeneOff_status.png", confidence=0.9)
        pygui.click(x=point_x, y=point_y)
        print("Turned generator on")
        sleep(1)