# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:14:53 2022

@author: vinch
"""

#pixel grabber

from time import sleep
import pyautogui as pygui

while True:
    _input = input("y/n")
    if _input == "y":
        sleep(3)

        print("Position: " + str(pygui.position()))
    