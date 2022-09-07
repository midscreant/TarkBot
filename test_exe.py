# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:11:55 2022

@author: vinch
"""

from Hideout import Hideout as Ho
from BootUp import BootUp as Bu
from time import sleep

my_hideout = Ho()


my_booter = Bu()

sleep(3)
# my_booter.runExe()
# sleep(7)
# print('a')
# my_booter.pressPlay()
# buttons = my_booter.checkForButtons()
# if buttons == None:
# statuses = my_hideout.findAllStatuses()
# print(statuses)y
print(my_hideout.makeBp())



  
#NOTES FOR TOMORROW
#Cut statuses down to locked, incomplete(this includes working), complete and na. will need to rename images 
#last test [('air', 'locked'), ('booze', 'complete'), ('btc', 'working_empty'), ('generator', 'na'), 
#('heating', 'na'), ('illumination', 'na'), ('intel', 'incomplete'), 
#('lav', 'working_full'), ('library', None),  ('med', 'complete'), ('nutrition', None), 
#('rest', 'na'), ('scav', 'incomplete'),  ('vents', 'na'), ('water', 'complete'), 
#('workbench', 'working_full')]
    # library and nutrition failed fully
    #scav was wrong, water was wrong, intel was incorrect
    #fine tune confidence var
    #can reuse functions from hideout to grab locations of nodes
    #Incomplete = Can be started
    #Complete = Claim, restart if need be
    #Na = No activity
    #Locked = Nothing
    #All of these should also be able to upgrade/construct if wanted
#Should also grab levels
#Add money info scraper 
#Make a general flea market purchase function
    #one that is a right click guide
    ##other is the button on bottom plus a text entry
#to start a recipe, scroll and look for image. create "recipe book" dict for reference
#grab y value & click start. may need to scroll too    

