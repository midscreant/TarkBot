# -*- coding: utf-8 -*-

#ORCHESTRATOR

from Hideout import Hideout
from ErrorChecker import ErrorChecker

import os
from time import time
from time import sleep
import pyautogui as pygui


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
        self.water_count = ("water",preset_dict["water"])
        self.booze_count = ("booze",preset_dict["booze"])
        self.generator_count = ("generator",preset_dict["generator"])
        
        self.quicksort_bool = preset_dict["quicksort"]
        self.flea_bool = preset_dict["flea"]
        self.insurance_bool = preset_dict["insurance"]
        self.reboot_bool = preset_dict["reboot"]
        
        self.runtime = preset_dict["runtime"]
        if self.runtime != -1:
            self.runtime = self.runtime * 900
            print("RUNTIME: " + str(self.runtime))
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
            print("Workbench run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.workbench_tuple[1][0]) 
        if status == "fail":
            print("Error: Workbench failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        elif status == "buy_fail":
            return "buy_fail"
        self.workbench_runs += 1
        
    def runIntel(self):
        if self.intel_runs == self.intel_tuple[1][1]:
            print("Intel run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.intel_tuple[1][0]) 
        if status == "fail":
            print("Error: Intel failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        elif status == "buy_fail":
            return "buy_fail"
        self.intel_runs += 1

    
    def runMed(self):
        if self.med_runs == self.med_tuple[1][1]:
            print("Medstation run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.med_tuple[1][0]) 
        if status == "fail":
            print("Error: Medstation failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        elif status == "buy_fail":
            return "buy_fail"
        self.med_runs += 1
    
    def runLav(self):
        if self.lav_runs == self.lav_tuple[1][1]:
            print("Lavatory run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.lav_tuple[1][0]) 
        if status == "fail":
            print("Error: Lavatory failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        elif status == "buy_fail":
            return "buy_fail"
        self.lav_runs += 1
        
    def runNutrition(self):
        if self.nutrition_runs == self.nutrition_tuple[1][1]:
            print("Nutrition run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.nutrition_tuple[1][0]) 
        if status == "fail":
            print("Error: Nutrition failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        elif status == "buy_fail":
            return "buy_fail"
        self.nutrition_runs += 1
        
    def runScav(self):
        if self.scav_runs == self.scav_tuple[1][1]:
            print("Scav case run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.makeRecipe, self.scav_tuple[1][0]) 
        if status == "fail":
            print("Error: Scav Case failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        elif status == "buy_fail":
            return "buy_fail"
        self.scav_runs += 1
        
    def runWater(self):
        if self.water_runs == self.water_count[1]:
            print("Water run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.waterChecker) 
        if status == "fail":
            print("Error: Water failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.water_runs += 1
        
    def runBooze(self):
        if self.booze_runs == self.booze_count[1] and self.booze_count[1] >= 0:
            print("Booze run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.boozeChecker) 
        if status == "fail":
            print("Error: Booze failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.booze_runs += 1
        
    def runGenerator(self):
        if self.generator_runs == self.generator_count[1] and self.generator_count[1] >= 0:
            print("Generator run count already reached")
            return
        status = self.my_checker.errorChecker(self.my_hideout.generatorChecker) 
        if status == "fail":
            print("Error: Generator failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.generator_runs += 1
        
    def runBtc(self): 
        status = self.my_checker.errorChecker(self.my_hideout.btcChecker)
        if status == "fail":
            print("Error: BTC failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.btc_runs += 1
        
    def runQuicksort(self):
        status = self.my_hideout.quickOrganizeInv()
        #doesnt run 3 times 
        if status == "fail":
            print("Error: Quicksort failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.quicksort_runs += 1
        
    def runFleaClaim(self):
        status = self.my_checker.errorChecker(self.my_hideout.claimFlea)
        if status == "fail":
            print("Error: Flea failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.flea_runs += 1
        
    def runInsuranceClaim(self):
        status = self.my_checker.errorChecker(self.my_hideout.claimInsurance)
        if status == "fail":
            print("Error: Insurance failure. Aborting attempt")
            return 'fail'
        elif status == "FATAL":
            return "FATAL"
        self.insurance_runs += 1
        
    def runAll(self, reset_value=None):
        _reset = reset_value
        run_list = [self.generator_count, self.workbench_tuple, self.intel_tuple, self.med_tuple, self.nutrition_tuple, self.lav_tuple, self.scav_tuple, self.water_count, self.booze_count]
        end_list = []
        for item in run_list:
            if type(item[1]) == tuple:
                if item[1][0] != None and item[1][1] != None:
                    end_list.append(item)
            elif item[1] != None:
                end_list.append(item)
                
        if self.quicksort_bool == True and (_reset == None or _reset == "quicksort"):
            if self.runQuicksort() == "FATAL":
                return ("FATAL", "quicksort")
            _reset = None
        if self.flea_bool == True and (_reset == None or _reset == "flea"):
            if self.runFleaClaim() == "FATAL":
                return ("FATAL", "flea")
            _reset = None
        if self.insurance_bool == True and (_reset == None or _reset == "insurance"):
            if self.runInsuranceClaim() == "FATAL":
                return ("FATAL", "insurance")
            _reset = None
        if _reset == None or _reset == "btc":
            if self.runBtc() == "FATAL":
                return ("FATAL", "btc")
            _reset = None
            
        self.my_hideout.geneOnCheck()
        for item in end_list:
            if item[0] == "generator" and (_reset == None or _reset == "generator"):
                status = self.runGenerator()
                if status == "FATAL":
                    return ("FATAL", "generator")
                _reset = None
                self.generator_runs += 1
                if self.my_hideout.checkForNoFuel() == "FATAL":
                    return ("FATAL", "kill")
            
            elif self.my_hideout.checkForNoFuel() == "FATAL":
                #maybe change to any node
                return ("FATAL", "kill")
            
            if item[0] == "workbench" and (_reset == None or _reset == "workbench"):
                status = self.runWorkbench()
                if status == "FATAL":
                    return ("FATAL", "workbench")
                elif status == "buy_fail":
                    self.workbench_tuple[1][0] == None
                _reset = None
            elif item[0] == "intel" and (_reset == None or _reset == "intel"):
                status = self.runIntel()
                if status == "FATAL":
                    return ("FATAL", "intel")
                elif status == "buy_fail":
                    self.intel_tuple[1][0] == None
                _reset = None
            elif item[0] == "med" and (_reset == None or _reset == "med"):
                status = self.runMed()
                if status == "FATAL":
                    return ("FATAL", "med")
                elif status == "buy_fail":
                    self.med_tuple[1][0] == None
                _reset = None
            elif item[0] == "nutrition" and (_reset == None or _reset == "nutrition"):
                status = self.runNutrition()
                if status == "FATAL":
                    return ("FATAL", "nutrition")
                elif status == "buy_fail":
                    self.nutrition_tuple[1][0] == None
                _reset = None
            elif item[0] == "lav" and (_reset == None or _reset == "lav"):
                status = self.runLav()
                if status == "FATAL":
                    return ("FATAL", "lav")
                elif status == "buy_fail":
                    self.lav_tuple[1][0] == None
                _reset = None
            elif item[0] == "scav" and (_reset == None or _reset == "scav"):
                status = self.runScav()
                if status == "FATAL":
                    return ("FATAL", "scav")
                elif status == "buy_fail":
                    self.scav_tuple[1][0] == None
                _reset = None
            elif item[0] == "water" and (_reset == None or _reset == "water"):
                status = self.runWater()
                if status == "FATAL":
                    return ("FATAL", "water")
                _reset = None
            elif item[0] == "booze" and (_reset == None or _reset == "booze"):
                status = self.runBooze()
                if status == "FATAL":
                    return ("FATAL", "booze")
                _reset = None
            else:
                print("ERROR: Incorrect node name. Ending run...")
                return ("FATAL", "kill")
            print(item[0].capitalize() + " run complete")
            print("\n")
            print("++++++++++++++++++++++++++++++++")
            sleep(10)
            #GIVES 10 SEC BETWEEN EACH MAKE TO ALLOW FOR QUITTING
        
        return "success"
            
    def orchestrator(self, reset_value=None):
        _reset = reset_value
        while True:
            current_time = time()
            if current_time - self.initial_epoch >= self.runtime and self.runtime != -1:
                break
            #At this point, program assumes you are on tarkov fully loaded home page 
            #if reset_value = getAll, don't need to change anything
            if _reset == None or _reset == "getAll":
                status = self.my_hideout.getAllItems() 
                if status == "FATAL":
                    return ("FATAL", "getAll")
                status = self.runAll()
                if status != "success":
                    return "FATAL"
                current_time = time()
                if current_time - self.repeat_epoch >= 900 * self.checkupFreq:
                    print("ERROR: Program took more than wait interval to complete. Ending run...")
                    return ("FATAL", "kill")
                
                sleep_value = 900 * self.checkupFreq - (current_time - self.initial_epoch)
                print("Loop complete. Time til next checkup: " + str(round(sleep_value, 2)) + "s")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-")
                sleep(sleep_value)
                self.repeat_epoch = time()
                
            else:
                if self.my_hideout.goToMainMenu() == "FATAL":
                    print("ERROR: Was not able to reset orchestrator. Ending run...")
                    return "FATAL"
                status = self.runAll(reset_value=_reset)
                if status != "success":
                    return "FATAL"
                current_time = time()
                if current_time - self.repeat_epoch >= 900 * self.checkupFreq:
                    print("ERROR: Program took more than wait interval to complete. Ending run...")
                    return ("FATAL", "kill")
                
                sleep_value = 900 * self.checkupFreq - (current_time - self.initial_epoch)
                print("Loop complete. Time til next checkup: " + str(round(sleep_value, 2)) + "s")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-")
                sleep(sleep_value)
                self.repeat_epoch = time()
                _reset = None
                
        return ("complete", "kill")
    
    def grabTotalTime(self):
        current_time = time()
        total_time = current_time - self.initial_epoch
        return total_time