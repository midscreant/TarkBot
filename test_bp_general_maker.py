# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:42:46 2022

@author: vinch
"""

#GENERAL PURPSOE MAKE BP


#GENERATOR FILL FUNCT
    #Check for open slots
    #Go to far right middle of the img found to click button
    #Attempt to add fuel
    #If no fuel, go buy jaeger's fuel on market
        #Go to flea, then look for entire jaeger offer, stop @ expires. find far right middle and move ~200px right
    #return to hideout and add




#<><><><><><><><><>
#ALL IMAGES
#<><><><><><><><><>

#workbench_list pics (can be used for all recipes) 
#BPExitLoop - uses a 762 icon pic "762bp_item_icon.png"
#"MultitoolReady_item_icon.png" - should take a list of all these pics to check, as some recipes will have 2 prereqs
#Need to also add "Buy n" of amount at once for big ammo counts 
#"MultitoolNotReady_item_icon.png"
#"762BPStart_recipe.png"


def bottomFlea(self):
    pygui.click(x=1228, y=1066)
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
        self.buyOnFlea(count)        
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
 

def makeRecipe(self, recipe):
    
    #untested, good start though
    #currently only does workbench
    
    #recipe is a dict
        #{"item_name": item_name , "repeats":[str1,str2*,str3*] , "item_info":{_item_name:item_count} , "start":"item_nameStart_Recipe.png" }
 
    #Takes you to hideout from home screen
    pygui.press('esc')
    sleep(0.1)
    pygui.press('esc')
    sleep(0.1)
    pygui.press('esc')
    sleep(0.1)
    pygui.press('esc') 
    sleep(0.5)
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
            os.chdir(self.recipes)
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
    
    
    
 