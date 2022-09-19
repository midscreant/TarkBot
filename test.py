# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:12:56 2022

@author: vinch
"""

import psutil

process_names = ["EscapeFromTarkov_BE.exe", "EscapeFromTarkov.exe", "BsgLauncher.exe"]

for proc in psutil.process_iter():
    if proc.name() in process_names:
        proc.kill()
        print("Killed " + proc.name() + " instance")
        process_names.pop(process_names.index(proc.name()))
print("All killed")
    
