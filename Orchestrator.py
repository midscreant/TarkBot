# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:16:29 2022

@author: vinch
"""

#TEST ORCHESTRATOR

from Hideout import Hideout
from ErrorChecker import ErrorChecker
from time import time
from time import sleep
import keyboard
    #-1 means the whole time

# {"workbench":(recipe_name, run_count), "intel":(recipe_name, run_count), "med":(recipe_name, run_count), 
#  "lav":(recipe_name, run_count), "nutrition":(recipe_name, run_count), "scav":(recipe_name, run_count), 
#  "booze":run_count (may be -1, which means run the whole time. same w others), "water":run_count,, 
#  "generator":run_count (represents how many big cans to add throughout run. -1 means always keep filled w/ at least 1 tank), 
#  "air":run_count (almost always gonna be 0),
#  "runtime":runtime, "checkup":checkup }+

class Orchestrator:
    
    def __init__(self, preset_dict):
        
        self.workbench_tuple = ("workbench",preset_dict["workbench"])
        self.intel_tuple = ("intel", preset_dict["intel"])
        self.med_tuple = ("med", preset_dict["med"])
        self.lav_tuple = ("lav", preset_dict["lav"])
        self.nutrition_tuple = ("nutrition", preset_dict["nutrition"])
        #scav names are MOON, 950, 25, 150, INTEL
        self.scav_tuple = ("scav", preset_dict["scav"]) 
        #claim water b4 booze on pulls to save $
        self.water_count = ("water",preset_dict["water"])
        self.booze_count = ("booze",preset_dict["booze"])
        self.generator_count = ("generator",preset_dict["generator"])
        # self.air_count = ("air",preset_dict["air"])
        
        [self.workbench_tuple, self.intel_tuple, self.med_tuple, self.lav_tuple, self.nutrition_tuple, self.scav_tuple, self.water_count, self.booze_count, self.generator_count]
        
        #if runtime is not set, run count MUST be established for each item. no infinite unless runtime set to that
        #runtime should be in seconds
        self.runtime = preset_dict["runtime"]
        #increments of 15 min X checkup (15min = 900s)
        self.checkupFreq = preset_dict["checkup"]
        
        self.workbench_runs = 0
        self.intel_runs = 0
        self.med_runs = 0
        self.lav_runs = 0
        self.nutrition_runs = 0
        self.scav_runs = 0
        self.booze_runs = 0
        self.water_runs = 0
        self.generator_runs = 0
        self.air_runs = 0
        self.btc_runs = 0
        
        self.my_hideout = Hideout()
        self.my_checker = ErrorChecker()
        self.initial_epoch = time()
        
        
    def runWorkbench(self):
        if self.workbench_runs == self.workbench_tuple[1][1]:
            print("Workbench run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("makeRecipe", 0, self.workbench_tuple[1][0]) 
            if status == "MEGAFAIL":
                print("Error: Workbench failure. Aborting attempt...")
                return 'fail'
            self.workbench_runs += 1
        except:
            print("Error: Fatal error while running workbench")
            return 'fail'
        
    def runIntel(self):
        if self.intel_runs == self.intel_tuple[1][1]:
            print("Intel run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("makeRecipe", 0, self.intel_tuple[1][0]) 
            if status == "MEGAFAIL":
                print("Error: Intel failure. Aborting attempt...")
                return 'fail'
            self.intel_runs += 1
        except:
            print("Error: Fatal error while running intel")
            return 'fail'
    
    def runMed(self):
        if self.med_runs == self.med_tuple[1][1]:
            print("Medstation run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("makeRecipe", 0, self.med_tuple[1][0]) 
            if status == "MEGAFAIL":
                print("Error: Medstation failure. Aborting attempt...")
                return 'fail'
            self.med_runs += 1
        except:
            print("Error: Fatal error while running medstation")
            return 'fail'
    
    def runLav(self):
        if self.lav_runs == self.lav_tuple[1][1]:
            print("Lavatory run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("makeRecipe", 0, self.lav_tuple[1][0]) 
            if status == "MEGAFAIL":
                print("Error: Lavatory failure. Aborting attempt...")
                return 'fail'
            self.lav_runs += 1
        except:
            print("Error: Fatal error while running lavatory")
            return 'fail'
        
    def runNutrition(self):
        if self.nutrition_runs == self.nutrition_tuple[1][1]:
            print("Nutrition run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("makeRecipe", 0, self.nutrition_tuple[1][0]) 
            if status == "MEGAFAIL":
                print("Error: Nutrition failure. Aborting attempt...")
                return 'fail'
            self.nutrition_runs += 1
        except:
            print("Error: Fatal error while running nutrition")
            return 'fail'
        
    def runScav(self):
        if self.scav_runs == self.scav_tuple[1][1]:
            print("Scav case run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("runScavCase", 0, self.scav_tuple[1][0]) 
            if status == "MEGAFAIL":
                print("Error: Scav Case failure. Aborting attempt...")
                return 'fail'
            self.scav_runs += 1
        except:
            print("Error: Fatal error while running scav case")
            return 'fail'
        
    def runWater(self):
        if self.water_runs == self.water_count[1]:
            print("Water run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("waterChecker" ) 
            if status == "MEGAFAIL":
                print("Error: Water failure. Aborting attempt...")
                return 'fail'
            self.water_runs += 1
        except:
            print("Error: Fatal error while running water")
            return 'fail'
        
    def runBooze(self):
        if self.booze_runs == self.booze_count[1]:
            print("Booze run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("boozeChecker" ) 
            if status == "MEGAFAIL":
                print("Error: Booze failure. Aborting attempt...")
                return 'fail'
            self.booze_runs += 1
        except:
            print("Error: Fatal error while running booze")
            return 'fail'
        
    def runGenerator(self):
        if self.generator_runs == self.generator_count[1]:
            print("Generator run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("generatorChecker" ) 
            if status == "MEGAFAIL":
                print("Error: Generator failure. Aborting attempt...")
                return 'fail'
            self.generator_runs += 1
        except:
            print("Error: Fatal error while running generator")
            return 'fail'
        
    def runAir(self):
        if self.air_runs == self.air_count[1]:
            print("Air run count already reached...")
            return
        try:
            status = self.my_checker.errorChecker("airChecker" ) 
            if status == "MEGAFAIL":
                print("Error: Air failure. Aborting attempt...")
                return 'fail'
            self.air_runs += 1
        except:
            print("Error: Fatal error while running air")
            return 'fail'
        
    def runBtc(self): 
        try:
            status = self.my_checker.errorChecker("btcChecker" ) 
            if status == "MEGAFAIL":
                print("Error: BTC failure. Aborting attempt...")
                return 'fail'
            self.btc_runs += 1
        except:
            print("Error: Fatal error while running BTC")
            return 'fail'
        
    def runAll(self):
        run_list = [self.workbench_tuple, self.intel_tuple, self.med_tuple, self.lav_tuple, self.nutrition_tuple, self.scav_tuple, self.water_count, self.booze_count, self.generator_count]
        end_list = []
        for item in run_list:
            if item[1] != None:
                #This means the user wants this service to run
                end_list.append(item)
                #adds full item to list, including name
        self.runBtc()        
        for item in end_list:
            if item[0] == "generator":
                self.runGenerator()
            elif item[0] == "workbench":
                self.runWorkbench()
            elif item[0] == "intel":
                self.runIntel()
            elif item[0] == "med":
                self.runMed()
            elif item[0] == "lav":
                self.runLav()
            elif item[0] == "nutrition":
                self.runNutrition()
            elif item[0] == "scav":
                self.runScav()
            elif item[0] == "water":
                self.runWater
            elif item[0] == "booze":
                self.runBooze()
            elif item[0] == "air":
                self.runAir()
            else:
                print("Error: Somehow incorrect node name??")
                return 'fail'
            
    def orchestrator(self):
        #HERE IS WHERE BOOT FUNCTIONS WOULD GO
        while True:
            current_time = time()
            if current_time - self.initial_epoch >= self.runtime:
                print("End of script reached. Alloted time: "+str(int(current_time - self.initial_epoch))+" seconds. Thank you for choosing TarkBot!")
                break
            if keyboard.is_pressed("Esc"):
                print("Exit key pressed. Alloted time: "+str(int(current_time - self.initial_epoch))+" seconds. Thank you for choosing TarkBot!")
                break 
            #At this point, program assumes you are on tarkov fully loaded home page 
            self.runAll()
            sleep(900 * self.checkupFreq)
        
        
        