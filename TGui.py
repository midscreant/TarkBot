# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:10:43 2022

@author: vinch
"""

from BootUp import BootUp
from Orchestrator import Orchestrator
from recipes___ import all_recipes

import tkinter as tk
from tkinter import filedialog as fd
from time import sleep
import os
import psutil
import ast
# import hashlib

# {"workbench":(workbench_value, workbench_count), "intel":(intel_value, intel_count), "med":(med_value, med_count), 
#  "lav":(lav_value, lav_count), "nutrition":(nutrition_value, nutrition_count), "scav":(scav_value, scav_count), 
#  "booze":booze_count (may be -1, which means run the whole time. same w others), "water":water_count, 
#  "generator":generator_count (represents how many big cans to add throughout run. -1 means always keep filled w/ at least 1 tank), 
#  "air":air_count (almost always gonna be 0),
#  "runtime":time_count, "checkup":checkup_count }+

class TGui:
    
    def __init__(self):
        
        self.root_path = os.getcwd()
        self.presets_path = os.path.join(self.root_path, "Presets")
        
        #INITIAL CREATION
        self.root_window = tk.Tk()
        self.root_window.minsize(800, 675)
        self.root_window.title("TarkBot v1.0")
        
        os.chdir(self.presets_path)
        #all file names without extension
        self.preset_files = [f for f in os.listdir('.') if os.path.isfile(f)]
        self.preset_names = []
        for filename in self.preset_files:
            if filename.endswith(".txt"):
                self.preset_names.append(filename[:-4])
        if len(self.preset_names) == 0:
            self.preset_names.append("No presets found...")
        print(self.preset_names)
            
        os.chdir(self.root_path)
        

        #MISSING LAVATORY AND AIR - should just cut air who tf is gonna run air remotely
            # next step is advanced error checking and bug testing
                #error checking at major spots
                    #may wanna check status of working nodes after starting to confirm
            #after that is captcha problem
                #try ocr text -> url strat
            
        #VARIABLE CREATION
        self.time_count = tk.StringVar()
        self.checkup_count = tk.StringVar()
        self.generator_count = tk.StringVar()
        self.workbench_count = tk.StringVar()
        self.intel_count = tk.StringVar()
        self.med_count = tk.StringVar()
        self.lav_count = tk.StringVar()
        self.nutrition_count = tk.StringVar()
        self.scav_count = tk.StringVar()
        self.water_count = tk.StringVar()
        self.booze_count = tk.StringVar()

        self.main_preset_value = tk.StringVar()
        self.sub_preset_value = tk.StringVar()
        self.path_value = None
        self.workbench_value = tk.StringVar()
        self.intel_value = tk.StringVar()
        self.med_value = tk.StringVar()
        self.lav_value = tk.StringVar()
        self.nutrition_value = tk.StringVar()
        self.scav_value = tk.StringVar()
        #OTHER THAN PRESET, VALUE HOLDS RECIPE NAME. CAN BE GIVEN DIRECTLY TO MAKE RECIPE
        
        self.return_value = None
        
        self.var_to_node_name = {}

        self.main_preset_value.set("Select an Option...")
        self.workbench_value.set("Select an Option...")
        self.intel_value.set("Select an Option...")
        self.med_value.set("Select an Option...")
        self.lav_value.set("Select an Option...")
        self.nutrition_value.set("Select an Option...")
        self.scav_value.set("Select an Option...")

        #recipe dicts
        self.workbench_recipes = all_recipes["Workbench"]
        self.nutrition_recipes = all_recipes["Nutrition"]
        self.intel_recipes = all_recipes["Intel"]
        self.medstation_recipes = all_recipes["Medstation"]

        #complete dicts
        self.full_workbench_recipes = self.workbench_recipes[0] | self.workbench_recipes[1] | self.workbench_recipes[2] 
        self.full_nutrition_recipes = self.nutrition_recipes[0] | self.nutrition_recipes[1] | self.nutrition_recipes[2]
        self.full_intel_recipes = self.intel_recipes[0] | self.intel_recipes[1]
        self.full_medstation_recipes = self.medstation_recipes[0] | self.medstation_recipes[1] | self.medstation_recipes[2]

        #complete name lists
        self.full_workbench_names = ["Select an Option..."] + list(self.full_workbench_recipes.keys() )
        self.full_nutrition_names = ["Select an Option..."] + list(self.full_nutrition_recipes.keys())
        self.full_intel_names = ["Select an Option..."] + list(self.full_intel_recipes.keys())
        self.full_medstation_names = ["Select an Option..."] + list(self.full_medstation_recipes.keys())
        self.full_scav_names = ["Select an Option..."] + list(all_recipes["Scav - Names"].values())

        #name - name dicts
        self.workbench_names = all_recipes["Workbench - Names"]
        self.nutrition_names = all_recipes["Nutrition - Names"]
        self.intel_names = all_recipes["Intel - Names"]
        self.medstation_names = all_recipes["Medstation - Names"]
        self.scav_names = all_recipes["Scav - Names"]

        #misc
        self.process_names = ["EscapeFromTarkov_BE.exe", "EscapeFromTarkov.exe", "BsgLauncher.exe"]
        self.all_nodes = ["generator", "workbench", "intel", "med", "lav", "nutrition", "scav", "water", "booze"]
        self.names_to_full = {"workbench":self.full_workbench_recipes, "nutrition":self.full_nutrition_recipes, "intel":self.full_intel_recipes, "med":self.full_medstation_recipes, "scav":self.scav_names}

        #COLUMN 0
        
        self.main_label = tk.Label(self.root_window, font=("Arial Bold", 20), text="TarkBot v1.0")
        self.main_label.grid(column=0, row=0, padx=(2.5, 100), pady=5)
        self.main_sublabel = tk.Label(self.root_window, font=("Arial", 8), text="Unplug all but one monitor")
        self.main_sublabel.grid(column=0, row=1)
        
        self.preset_label = tk.Label(self.root_window, text="Preset", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.preset_label.grid(column=0, row=2, padx=2.5, pady=5)
        self.preset_menu = tk.OptionMenu(self.root_window, self.main_preset_value, *self.preset_names)
        self.preset_menu.grid(column=0, row=3, padx=2.5, pady=5)
        self.preset_set_button = tk.Button(self.root_window, text="Insert", command=self.setPreset)
        self.preset_set_button.grid(column=0, row=4, padx=2.5, pady=5)
        self.preset_delete_button = tk.Button(self.root_window, text="Delete", command=self.deletePreset)
        self.preset_delete_button.grid(column=0, row=5, padx=2.5, pady=5)
        self.lower_preset_label  = tk.Label(self.root_window)
        self.lower_preset_label.grid(column=0, row=6, padx=2.5, pady=5)
        
        self.time_label = tk.Label(self.root_window, text="Time (15min x Entry)", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.time_label.grid(column=0, row=8, padx=2.5, pady=5)
        self.time_entry = tk.Entry(self.root_window, textvariable=self.time_count, width=35, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.time_entry.grid(column=0, row=9, padx=2.5, pady=5)
        
        self.checkup_label = tk.Label(self.root_window, text="Checkup Freq (15min x Entry)", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.checkup_label.grid(column=0, row=11, padx=2.5, pady=5)
        self.checkup_entry = tk.Entry(self.root_window, textvariable=self.checkup_count, width=35, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.checkup_entry.grid(column=0, row=12, padx=2.5, pady=5)
        
        self.path_label = tk.Label(self.root_window, text="Path to BSGLauncher.exe", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.path_label.grid(column=0, row=14, padx=2.5, pady=5)
        self.path_space = tk.Label(self.root_window)
        self.path_space.grid(column=0, row=15, padx=2.5, pady=5)
        def selectFile():
            file_path = fd.askopenfilename(initialdir="/", title="Find bsglauncher.exe", filetypes=(("Executables (.exe)", "*.exe"),))
            self.path_space["text"] = file_path
            self.path_value = file_path
            #in future, save this to a txt file as saved config
        self.select_button = tk.Button(self.root_window, text="Select file", width=10, command=selectFile)
        self.select_button.grid(column=0, row=16, padx=2.5, pady=5)
        
        self.time_label = tk.Label(self.root_window,font=("Arial Bold", 15))
        self.time_label.grid(column=0, row=17, rowspan=5)
        
        self.start_label = tk.Label(self.root_window, font=("Arial", 10))
        self.start_label.grid(column=0, row=23)
        self.start_button = tk.Button(self.root_window, text="Start", command=self.startPressed, width=25, height=2, font=("Arial Bold", 12))
        self.start_button.grid(column=0, row=24, padx=25, pady=(0, 10))
        
        
        #COLUMN 1
        
        self.main_label_2 = tk.Label(self.root_window, font=("Arial Bold", 15), text="Nodes")
        self.main_label_2.grid(column=1, row=0, padx=2.5, pady=1, columnspan=2)
        
        self.sublabel = tk.Label(self.root_window, text="A negative run count will run node\nfor as long as program runs", font=("Arial", 8))
        self.sublabel.grid(column=1, row=1, padx=2.5, pady=(0,5), columnspan=2)
        
        self.generator_label = tk.Label(self.root_window, text="Generator (n x BigFuel)", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.generator_label.grid(column=1, row=2)
        self.generator_entry = tk.Entry(self.root_window, textvariable=self.generator_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.generator_entry.grid(column=1, row=3, padx=2.5, pady=5)
        
        self.water_label = tk.Label(self.root_window, text="Water (n x Filter)", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.water_label.grid(column=1, row=5)
        self.water_entry = tk.Entry(self.root_window, textvariable=self.water_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.water_entry.grid(column=1, row=6, padx=2.5, pady=5)
        
        self.booze_label = tk.Label(self.root_window, text="Booze", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.booze_label.grid(column=1, row=8)
        self.booze_entry = tk.Entry(self.root_window, textvariable=self.booze_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.booze_entry.grid(column=1, row=9, padx=2.5, pady=5)
        
        
        #COLUMN 2
        
        self.workbench_label = tk.Label(self.root_window, text="Workbench", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.workbench_label.grid(column=2, row=2)
        self.workbench_menu = tk.OptionMenu(self.root_window, self.workbench_value, *self.full_workbench_names)
        self.workbench_menu.grid(column=2, row=3)
        self.workbench_entry = tk.Entry(self.root_window, textvariable=self.workbench_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.workbench_entry.grid(column=2, row=4, padx=2.5, pady=5)
        
        self.intel_label = tk.Label(self.root_window, text="Intel", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.intel_label.grid(column=2, row=5)
        self.intel_menu = tk.OptionMenu(self.root_window, self.intel_value, *self.full_intel_names)
        self.intel_menu.grid(column=2, row=6)
        self.intel_entry = tk.Entry(self.root_window, textvariable=self.intel_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.intel_entry.grid(column=2, row=7, padx=2.5, pady=5)
        
        self.med_label = tk.Label(self.root_window, text="Medstation", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.med_label.grid(column=2, row=8)
        self.med_menu = tk.OptionMenu(self.root_window, self.med_value, *self.full_medstation_names)
        self.med_menu.grid(column=2, row=9)
        self.med_entry = tk.Entry(self.root_window, textvariable=self.med_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.med_entry.grid(column=2, row=10, padx=2.5, pady=5)
        
        self.lav_label = tk.Label(self.root_window, text="Lavatory", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.lav_label.grid(column=2, row=11)
        self.lav_menu = tk.OptionMenu(self.root_window, self.lav_value, *self.preset_names)
        self.lav_menu.grid(column=2, row=12)
        self.lav_entry = tk.Entry(self.root_window, textvariable=self.lav_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.lav_entry.grid(column=2, row=13, padx=2.5, pady=5)
        
        self.nutrition_label = tk.Label(self.root_window, text="Nutrition", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.nutrition_label.grid(column=2, row=14)
        self.nutrition_menu = tk.OptionMenu(self.root_window, self.nutrition_value, *self.full_nutrition_names)
        self.nutrition_menu.grid(column=2, row=15)
        self.nutrition_entry = tk.Entry(self.root_window, textvariable=self.nutrition_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.nutrition_entry.grid(column=2, row=16, padx=2.5, pady=5)
        
        self.scav_label = tk.Label(self.root_window, text="Scav", font=("Arial Bold", 8), borderwidth=2, relief="ridge")
        self.scav_label.grid(column=2, row=17)
        self.scav_menu = tk.OptionMenu(self.root_window, self.scav_value, *self.full_scav_names)
        self.scav_menu.grid(column=2, row=18)
        self.scav_entry = tk.Entry(self.root_window, textvariable=self.scav_count, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self.scav_entry.grid(column=2, row=19, padx=2.5, pady=5)
        
        self._preset_label = tk.Label(self.root_window, text="Preset Name", font=("Arial Bold", 8))
        self._preset_label.grid(column=2, row=20, padx=2.5, pady=5)
        self._preset_label_2 = tk.Label(self.root_window, text="Leave blank to\nuse deafult", font=("Arial", 8))
        self._preset_label_2.grid(column=2, row=21, padx=2.5, pady=5)
        self._preset_name_entry = tk.Entry(self.root_window, textvariable=self.sub_preset_value, width=20, highlightthickness=1, highlightbackground="black", highlightcolor="red")
        self._preset_name_entry.grid(column=2, row=22, padx=2.5, pady=5)
        self._preset_save_button = tk.Button(self.root_window, text="Save", command=self.savePreset)
        self._preset_save_button.grid(column=2, row=23, padx=2.5, pady=2.5)
        
        
        self.root_window.mainloop()
        #call mainloop on class instance
        
    def updateMenu(self, option_menu, new_full_list):
        #new_full_list should be a list
        _menu = option_menu["menu"]
        _menu.delete(0, "end")
        for string in new_full_list:
            _menu.add_command(label=string, command=lambda value=string: self.main_preset_value.set(value))
    
    def savePreset(self):
        self.var_to_node_name = {"workbench":(self.workbench_value.get(), self.workbench_count.get()), 
                                 "intel":(self.intel_value.get(), self.intel_count.get()),
                                 "nutrition":(self.nutrition_value.get(), self.nutrition_count.get()),
                                 "med":(self.med_value.get(), self.med_count.get()), 
                                 # "lav":(self.lav_value, self.lav_count),
                                 "scav":(self.scav_value.get(), self.scav_count.get()), 
                                 "booze":self.booze_count.get(), 
                                 "water":self.water_count.get(), 
                                 "generator":self.generator_count.get(), 
                                 "runtime":self.time_count.get(), 
                                 "checkup":self.checkup_count.get(),
                                 "path":self.path_value}
        
        none_count = 0
        for key, value in list(self.var_to_node_name.items()):
            if key=="runtime" or key=="checkup" or key=="path":
                continue
            if type(value) == tuple:
                if value[0] == None or value[0] == "Select an Option...":
                    none_count += 1
                    continue
            elif value == None or value.strip() == "":
                none_count += 1
        
        if none_count >= len(self.var_to_node_name.keys()) - 3:
            self.start_label["text"] = "Error: Preset requires\ntime, checkup, path and at least 1 action"
            return 'fail'
                    
        return_dict = self.fullCheck()
        os.chdir(self.presets_path)
        file_list = [f for f in os.listdir('.') if os.path.isfile(f)]
        file_count = len(file_list)
        preset_name = self.sub_preset_value.get()
        if len(preset_name.strip()) > 0:
            try:
                file_string = preset_name + ".txt"
                with open(file_string, "x") as fp:
                    fp.write(str(return_dict))
            except:
                file_string = "Custom Preset " + str(file_count + 1) + ".txt"
                with open(file_string, "x") as fp:
                    fp.write(str(return_dict))
        else:
            file_string = "Custom Preset " + str(file_count + 1) + ".txt"
            with open(file_string, "x") as fp:
                fp.write(str(return_dict))
                
        # main_hash = hashlib.md5(file_string.encode())
        # print(main_hash.hexdigest())
        # for file in self.preset_files:
        #     second_hash = hashlib.md5(file.encode())
        #     print(second_hash.hexdigest())
        #     if main_hash.hexdigest() == second_hash.hexdigest():
        #         os.remove(file_string)
        #         print("Error: This exact preset already exists. Preset " + file)
        #         self._preset_label_2["text"] = "Error: This exact preset\nalready exists\nPreset " + file
        #         return 'fail'
                
        print("New preset created: " + file_string)
        self._preset_label_2["text"] = "New preset created: " + file_string[:-4]
        self.preset_names.append(file_string[:-4])
        self.updateMenu(self.preset_menu, self.preset_names)
        self.preset_files.append(file_string)

        os.chdir(self.root_path)
            
                
    
    def setPreset(self):
        
        if self.main_preset_value == "Select an Option...":
            print("Error: No preset selected")
            return
        
        preset_file = self.preset_menu["text"] + ".txt"
        print(preset_file)
        dict_string = ""
        os.chdir(self.presets_path)
        with open(preset_file, "r") as fp:
            for line in fp:
                dict_string = dict_string + line
                
        preset_dict = ast.literal_eval(dict_string.strip())
        # print(dict_string)
        
        #PRESET DICT STRUCTURE
            #{"name":preset_name, "runtime":count, "checkup":count, "path":path_to_launcher...}
            
        nodes_to_set = {}
        
        for key, value in list(preset_dict.items()):
            if type(value) == tuple:
                if value[0] == None:
                    continue
                nodes_to_set[key] = value
            elif type(value) == str or type(value) == int:
                nodes_to_set[key] = value
                    
        if "workbench" in nodes_to_set.keys():
            self.workbench_value.set(preset_dict["workbench"][0])
            self.workbench_count.set(int(preset_dict["workbench"][1]))
        if "scav" in nodes_to_set.keys():
            self.scav_value.set(preset_dict["scav"][0])
            self.scav_count.set(int(preset_dict["scav"][1]))
        if "intel" in nodes_to_set.keys():
            self.intel_value.set(preset_dict["intel"][0])
            self.intel_count.set(int(preset_dict["intel"][1]))
        if "med" in nodes_to_set.keys():
            self.med_value.set(preset_dict["med"][0])
            self.med_count.set(int(preset_dict["med"][1]))
        if "nutrition" in nodes_to_set.keys():
            self.nutrition_value.set(preset_dict["nutrition"][0])
            self.nutrition_count.set(int(preset_dict["nutrition"][1]))
        if "runtime" in nodes_to_set.keys():
            self.time_count.set(int(preset_dict["runtime"]))
        if "checkup" in nodes_to_set.keys():
            self.checkup_count.set(int(preset_dict["checkup"]))
        if "path" in nodes_to_set.keys():
            self.path_space["text"] = preset_dict["path"]
        if "generator" in nodes_to_set.keys():
            self.generator_count.set(int(preset_dict["generator"]))
        if "water" in nodes_to_set.keys():
            self.water_count.set(int(preset_dict["water"]))
        if "booze" in nodes_to_set.keys():
            self.booze_count.set(int(preset_dict["booze"]))
            
        # print(nodes_to_set)
        os.chdir(self.root_path)
        
    def deletePreset(self):
        os.chdir(self.presets_path)
        file_name = self.preset_menu["text"] + ".txt"
        if file_name in self.preset_files:
            try:
                os.remove(file_name)
                self.lower_preset_label["text"] = "Preset deleted: " + file_name[:-4]
            except:
                self.lower_preset_label["text"] = "Error while trying to delete preset"
        os.chdir(self.root_path)
                
                
            
        
        
    def countCheck(self, value):
        value_inside = None
        if type(value) != str and type(value) != int:
           value_inside = value.get()
        else:
           value_inside = value
        if "BsgLauncher" in value_inside:
            return value_inside
        try:
           count = int(value_inside.strip())
           if count <= -1:
               count = -1
           return count
        except:
           return None
       
    def nameCheck(self, value):
        value_inside = value
        if type(value_inside) != str:
            value_inside = value.get()
        if str(value_inside) != "Select an Option...":
            return str(value_inside)
        else:
            return None
        
    def fullCheck(self):
        return_dict = {}
        for name, value in list(self.var_to_node_name.items()):
            if type(value) == tuple:
                value_1 = self.nameCheck(value[0])
                value_2 = self.countCheck(value[1])
                if value_1 == None or value_2 == None:
                    value_1 = None
                    value_2 = None
                return_dict[name] = (value_1, value_2)
            else:
                value_1 = self.countCheck(value)
                return_dict[name] = value_1
        return return_dict
       
    def startPressed(self):
        self.var_to_node_name = {"workbench":(self.workbench_value.get(), self.workbench_count.get()), 
                                     "intel":(self.intel_value.get(), self.intel_count.get()),
                                     "nutrition":(self.nutrition_value.get(), self.nutrition_count.get()),
                                     "med":(self.med_value.get(), self.med_count.get()), 
                                     # "lav":(self.lav_value.get(), self.lav_count.get()),
                                     "scav":(self.scav_value.get(), self.scav_count.get()), 
                                     "booze":self.booze_count.get(), 
                                     "water":self.water_count.get(), 
                                     "generator":self.generator_count.get(), 
                                     "runtime":self.time_count.get(), 
                                     "checkup":self.checkup_count.get()} 
        
        if self.countCheck(self.time_count) == None or self.countCheck(self.checkup_count) == None:
            self.start_label["text"] = "Error: Time or checkup entry invalid. Must be int"
            # return 'fail'
        
        if self.path_space["text"].lower().endswith("bsglauncher.exe") != True:
            self.start_label["text"] = "Error: Invalid path selection"
            # return 'fail'
        
        self.start_label["text"] = " "
        
        self.start_return_dict = self.fullCheck()
        
        dict_string = ""
        for name, value in list(self.start_return_dict.items()):
            if name == "runtime" or name == "checkup":
                if value != -1:
                    dict_string = dict_string + name.upper() + " VALUE: " + str(int(value) * 15) + " MINUTES\n"
                else:
                    dict_string = dict_string + name.upper() + " VALUE: " + str(value) + "\n"
            else:
                dict_string = dict_string + name.upper() + " VALUE: " + str(value) + "\n"
        dict_string = dict_string + "_____________\n"
        pop_up_window = tk.Tk()
        pop_up_window.resizable(False, False)
        pop_up_window.title("Confirmation")
        
        title_label = tk.Label(pop_up_window, text="CONFIRMATION\n__________", font=("Arial Bold", 20))
        title_label.grid(column=0, row=0, padx=5, pady=(5,15))
        
        value_label = tk.Label(pop_up_window, text=dict_string, font=("Arial", 10))
        value_label.grid(column=0, row=1, padx=5, pady=(0,10))
        
        def confirm():
            pop_up_window.destroy()
            self.return_value = self.start_return_dict
            self.beginRun(self.return_value)
            
        
        confirm_button = tk.Button(pop_up_window, text="CONFIRM", command=confirm, width=20, height=2)
        confirm_button.grid(column=0, row=2, padx=5, pady=(0, 5))
        
        cancel_button = tk.Button(pop_up_window, text="CANCEL", command=pop_up_window.destroy, width=20, height=2)
        cancel_button.grid(column=0, row=3, padx=5, pady=(0, 5))

        
    def beginRun(self, value_dict):
        #BOOT GAME, WAIT FOR LOAD
        self.my_booter = BootUp(self.path_space["text"], self.root_path)
        boot_status = self.my_booter.fullRun()
        if boot_status != "success":
           self.start_label["text"] = "Error: Tarkov was not able to boot. Closing bot" 
           return 'fail'
       
        self._kill = False
        
        self.exit_window = tk.Tk()
        self.exit_window.geometry("+1250+5")
        
        def exitProgram():
            self.exit_window.destroy()
            self._kill = True
            #KILL EFT HERE
            #will need user to manually set eft installation path (exe not launcher)
            
            
        exit_button = tk.Button(self.exit_window, text="Exit", width=25, height=2, command=exitProgram, borderwidth=2, relief="ridge")
        exit_button.grid(row=0, column=0, padx=5, pady=2.5)
        
        self.exit_window.lift()
                
        my_orchestrator = Orchestrator(value_dict, self.root_path)
        status = my_orchestrator.orchestrator()
        if status == "FATAL":
            print("Exiting program due to fatal error...")
            exitProgram()
        #May need to call orchestrator within new tkinter main loop, as i dont think it will get to it otherwise
        #IDEA FOR EXIT KEY. BOOT HAPPENS, LOOKS FOR MAIN MENU. ONCE MAIN MENU FOUND, OPEN TKINTER WINDOW IN BOTTOM RIGHT, HAVE IT ALWAYS STAY ON SCREEN, MAKE EXIT KEY
        self.exit_window.mainloop()  
        
        if self._kill == True:
            self._kill == False
            total_time = my_orchestrator.grabTotalTime()
            self.time_label["text"] = "End of script reached.\nAlloted time: "+str(total_time)+" seconds.\nThank you for choosing TarkBot!"
            
            for proc in psutil.process_iter():
                if proc.name() in self.process_names:
                    print("Killing " + proc.name() + " instance")
                    proc.kill()
                    self.process_names.pop(self.process_names.index(proc.name()))
            
            if len(self.process_names) < 1:
                print("All relevant processes killed")
                print("End of script reached.\nAlloted time: "+str(total_time)+" seconds.\nThank you for choosing TarkBot!")
            else:
                print("End of script reached.\nAlloted time: "+str(total_time)+" seconds.\nThank you for choosing TarkBot!")
                print("\n\n\nERROR: not all processes killed. Must kill manually before new run")
    

my_gui = TGui()    
    
    
    
    
    
    
    
    
    
            