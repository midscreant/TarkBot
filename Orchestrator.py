# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:59:28 2022

@author: vinch
"""

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
    #-1 means the whole time

# {"workbench":(recipe_name, run_count), "intel":(recipe_name, run_count), "med":(recipe_name, run_count), 
#  "lav":(recipe_name, run_count), "nutrition":(recipe_name, run_count), "scav":(recipe_name, run_count), 
#  "booze":run_count (may be -1, which means run the whole time. same w others), "water":run_count,, 
#  "generator":run_count (represents how many big cans to add throughout run. -1 means always keep filled w/ at least 1 tank), 
#  "runtime":runtime, "checkup":checkup }+

class Orchestrator:
    
    def __init__(self, preset_dict, base_path):
        
        self.root_path = base_path
        
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
        
        self.quicksort_bool = preset_dict["quicksort"]
        self.flea_bool = preset_dict["flea"]
        self.insurance_bool = preset_dict["insurance"]
        self.reboot_bool = preset_dict["reboot"]
        
        #if runtime is not set, run count MUST be established for each item. no infinite unless runtime set to that
        self.runtime = preset_dict["runtime"]
        if self.runtime != -1:
            self.runtime = self.runtime * 900
            print("RUNTIME: " + str(self.runtime))
        #increments of 15 min X checkup (15min = 900s)
        self.checkupFreq = preset_dict["checkup"]
        if self.checkupFreq == -1:
            self.checkupFreq = 1
        
        self.workbench_runs = 0
        self.intel_runs = 0
        self.med_runs = 0
        self.lav_runs = 0
        self.nutrition_runs = 0
        self.scav_runs = 0
        self.booze_runs = 0
        self.water_runs = 0
        self.generator_runs = 0
        self.btc_runs = 0
        self.quicksort_runs = 0
        self.flea_runs = 0
        self.insurance_runs = 0
        self.reboot_runs = 0
        
        self.my_hideout = Hideout(self.root_path)
        self.my_checker = ErrorChecker()
        self.initial_epoch = time()
        
        self.repeat_epoch = self.initial_epoch
        
        
    def runWorkbench(self):
        if self.workbench_runs == self.workbench_tuple[1][1]:
            print("Workbench run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.workbench_tuple[1][0]) 
        if status == "fail":
            print("Error: Workbench failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.workbench_runs += 1
        
    def runIntel(self):
        if self.intel_runs == self.intel_tuple[1][1]:
            print("Intel run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.intel_tuple[1][0]) 
        if status == "fail":
            print("Error: Intel failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.intel_runs += 1

    
    def runMed(self):
        if self.med_runs == self.med_tuple[1][1]:
            print("Medstation run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.med_tuple[1][0]) 
        if status == "fail":
            print("Error: Medstation failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.med_runs += 1
        print("Error: Fatal error while running medstation")
        return 'fail'
    
    def runLav(self):
        if self.lav_runs == self.lav_tuple[1][1]:
            print("Lavatory run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.lav_tuple[1][0]) 
        if status == "fail":
            print("Error: Lavatory failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.lav_runs += 1
        
    def runNutrition(self):
        if self.nutrition_runs == self.nutrition_tuple[1][1]:
            print("Nutrition run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.nutrition_tuple[1][0]) 
        if status == "fail":
            print("Error: Nutrition failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.nutrition_runs += 1
        
    def runScav(self):
        if self.scav_runs == self.scav_tuple[1][1]:
            print("Scav case run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.scav_tuple[1][0]) 
        if status == "fail":
            print("Error: Scav Case failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.scav_runs += 1
        
    def runWater(self):
        if self.water_runs == self.water_count[1]:
            print("Water run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.waterChecker) 
        if status == "fail":
            print("Error: Water failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.water_runs += 1
        
    def runBooze(self):
        if self.booze_runs == self.booze_count[1]:
            print("Booze run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.boozeChecker) 
        if status == "fail":
            print("Error: Booze failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.booze_runs += 1
        
    def runGenerator(self):
        if self.generator_runs == self.generator_count[1]:
            print("Generator run count already reached...")
            return
        status = self.my_checker.errorChecker(self.my_hideout.generatorChecker) 
        if status == "fail":
            print("Error: Generator failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.generator_runs += 1
        
    def runBtc(self): 
        status = self.my_checker.errorChecker(self.my_hideout.btcChecker)
        if status == "fail":
            print("Error: BTC failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.btc_runs += 1
        
    def runQuicksort(self):
        status = self.my_checker.self.my_hideout.quickOrganizeInv()
        #doesnt run 3 times 
        if status == "fail":
            print("Error: Quicksort failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.quicksort_runs += 1
        
    def runFleaClaim(self):
        status = self.my_checker.errorChecker(self.my_hideout.claimFlea)
        if status == "fail":
            print("Error: Flea failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.flea_runs += 1
        
    def runInsuranceClaim(self):
        status = self.my_checker.errorChecker(self.my_hideout.claimInsurance)
        if status == "fail":
            print("Error: Insurance failure. Aborting attempt...")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.insurance_runs += 1
        
    def runAll(self):
        run_list = [self.generator_count, self.workbench_tuple, self.intel_tuple, self.med_tuple, self.nutrition_tuple, self.lav_tuple, self.scav_tuple, self.water_count, self.booze_count]
        end_list = []
        for item in run_list: 
            if type(item[1]) == tuple:
                if item[1][0] != None and item[1][1] != None:
                    end_list.append(item)
            elif item[1] != None:
                end_list.append(item)
                
        if self.quicksort_bool == True:
            if self.runQuicksort() == "FATAL":
                return "FATAL"
        if self.flea_bool == True:
            if self.runFleaClaim() == "FATAL":
                return "FATAL"
        if self.insurance_bool == True:
            if self.runInsuranceClaim() == "FATAL":
                return "FATAL"
            
        if self.runBtc() == "FATAL":
            return "FATAL"
        for item in end_list:
            if item[0] == "generator":
                status = self.runGenerator()
                if status == "FATAL":
                    return "FATAL"
            elif item[0] == "workbench":
                status = self.runWorkbench()
                if status == "FATAL":
                    return "FATAL"
            elif item[0] == "intel":
                status = self.runIntel()
                if status == "FATAL":
                    return "FATAL"
            elif item[0] == "med":
                status = self.runMed()
                if status == "FATAL":
                    return "FATAL"
            elif item[0] == "lav":
                status = self.runLav()
                if status == "FATAL":
                    return "FATAL"
            elif item[0] == "nutrition":
                status = self.runNutrition()
                if status == "FATAL":
                    return "FATAL"
            elif item[0] == "scav":
                status = self.runScav()
                if status == "FATAL":
                    return "FATAL"
            elif item[0] == "water":
                status = self.runWater()
                if status == "FATAL":
                    return "FATAL"
            elif item[0] == "booze":
                status = self.runBooze()
                if status == "FATAL":
                    return "FATAL"
            else:
                print("Error: Somehow incorrect node name??")
                return 'fail'
            print("Ran " + item[0])
            sleep(10)
            #GIVES 10 SEC BETWEEN EACH MAKE TO ALLOW FOR QUITTING
            
    def orchestrator(self):
        while True:
            current_time = time()
            if current_time - self.initial_epoch >= self.runtime and self.runtime != -1:
                break
            #At this point, program assumes you are on tarkov fully loaded home page 
            status = self.my_hideout.getAllItems()
            if status == "FATAL":
                return "FATAL"
            status = self.runAll()
            if status == "FATAL":
                return "FATAL"
            print("Run complete successfully")
            current_time = time()
            if current_time - self.repeat_epoch >= 900 * self.checkupFreq:
                print("ERROR: Program took more than wait interval to complete...")
                return "FATAL"
            
            sleep(900 * self.checkupFreq - (current_time - self.initial_epoch))
            self.repeat_epoch = time()
        return "complete"
    
    def grabTotalTime(self):
        current_time = time()
        total_time = current_time - self.initial_epoch
        return total_time
        
        
        