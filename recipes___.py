# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:55:05 2022

@author: vinch
"""

#recipe_dicts


#workbench_recipes = {item_name:{ingredient_1:count, ingredient_2, count...}, item_2_name...}
    #if item can be created with 2 recipes, second name will end will end in -_-
    
    
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#workbench    

workbench_1_recipes = {"Broken LCD":{"Screwdriver":1, "Working LCD":4},
                     "Printed Circuit Board":{"Flat Screwdriver":1, "DVD Drive":1},
                     "Printed Circuit Board-_-":{"Screwdriver":1, "Gas Analyzer":1},
                     "Power Cord":{"T-Shaped Plug":2, "Bundle of Wires":2, "Insulating Tape":1},
                     "Gunpowder \"Hawk\"":{"Gunpowder \"Kite\"":1, "Gunpowder \"Eagle\"":1, "Classic Matches":1},
                     "Magnet":{"Screwdriver":1, "Damaged Hard Drive":1},
                     "Gas Analyzer":{"Pliers Elite":1, "AA Battery":4, "Geiger-Muller counter":1, "Magnet":2, "Bundle of Wires":4},
                     "Weapon Parts":{"Flat Screwdriver":1, "Simonov SKS 7.62x39 carbine":1},
                     "Weapon Parts-_-":{"Leatherman Multitool":1, "Molot VPO-209 .366 TKM carbine":1},
                     "T-Shaped Plug":{"Power Cord":1, "Pack of Nails":1},
                     "Kalashnikov AK-74N 5.45x39 assault rifle":{"Screwdriver":1, "Pliers":1, "Weapon Parts":1, "AK-74 wooden handguard (6P20 Sb.6)":1, "AK-74 wooden stock (6P20 Sb.5)":1},
                     "Kalashnikov AKM 7.62x39 assault rifle":{"Set of files \"Master\"":1, "Leatherman Multitool":1, "Molot VPO-136 \"Vepr-KM\" 7.62x39 carbine":1, "AKM 7.62x39 muzzle brake & compensator (6P1 0-14)":1},
                     "Gunpowder \"Kite\"":{"Pliers":1, "5.45x39mm PS gs":70},
                     "12/70 8.5mm Magnum buckshot":{"Classic Matches":1, "Gunpowder \"Kite\"":1},
                     "Broken GPhone smartphone":{"Flat Screwdriver (Long)":1, "Broken GPhone X Smartphone":1, "Broken LCD":1},
                     "VOG-25 Khattabka improvised hand grenade":{"Leatherman Multitool":1, "UZRGM Grenade Fuze":5, "40mm VOG-25":5},
                     "9x18mm PM RG028 gzh":{"Gunpowder \"Kite\"":1},
                     "Bundle of wires":{"Power Cord":2},
                     "Capacitors":{"Screwdriver":1, "Power Supply Unit":1},
                     "PP-9 \"Klin\" 9x18PMM submachine gun":{"Set of files \"Master\"":1, "PP-91 \"Kedr\" 9x18PM submachine gun":1},
                     "Round Pliers":{"Set of Files \"Master\"":1, "Pliers":1} }

workbench_2_recipes = {"Rechargeable battery":{"Flat Screwdriver":1, "Portable Powerbank":1},
                       "GreenBat lithium battery":{"Round Pliers":1, "USB Adapter":3, "Rechargeable Battery":2, "Portable Powerbank":3},
                       "\"Zarya\" stun grenade":{"UZRGM Grenade Fuze":5, "Gunpowder \"Kite\"":1, "RDG-2B Smoke Grenade":1},
                       "Electric Motor":{"Screwdriver":1, "Flat Screwdriver":1, "Electric Drill":2, "Insulating Tape":2},
                       "Kalashnikov AK-74M 5.45x39 assault rifle":{"Toolset":1, "Weapon Parts":1, "AK-74 polymer handguard (6P20 Sb.9)":1, "AK-74M polymer stock (6P34 Sb.15)":1},
                       "Geiger-Muller counter":{"Toolset":1, "Gas Analyzer":1, "Bundle of Wires":1, "Capacitors":1, "AA Battery":1},
                       "Gunpowder \"Eagle\"":{"Screwdriver":1, "M67 Hand Grenade":2, "M18 Smoke Grenade (Green)":1},
                       "Gunpowder \"Hawk\"":{"Ratchet Wrench":1, "OFZ 30x160mm Shell":1, "Gunpowder \"Kite\"":2},
                       "Spark Plug":{"Pliers":1, "Screw Nuts":1, "Bolts":2, "SurvL Survivor Lighter":1},
                       "12/70 Flechette":{"Leatherman Multitool":1, "Metal Cutting Scissors":1, "Metal Fuel Tank":1, "Gunpowder \"Kite\"":1},
                       "Military Circuit Board":{"Pliers Elite":1, "Screwdriver":1, "Flat Screwdriver (Long)":1, "Military COFDM Wireless Signal Transmitter":1},
                       "NIXXOR Lens":{"Tech Manual":1, "Toolset":1, "Wi-Fi Camera":1, "Piece of Plexiglass":1},
                       "Car Battery":{"Pipe Grip Wrench":1, "6-STEN-140-M Military Battery":1},
                       "9x18mm PM PBM gzh":{"Toolset":1, "Gunpowder \"Kite\"":2, "9x18mm PM Pst gzh":200},
                       "12/70 SuperFormance HP slug":{"Leatherman Multitool":1, "Tech Manual":1, "Weapon Parts":1, "Gunpowder \"Kite\"":1},
                       "5.45x39mm PP gs":{"Nippers":1, "5.45x39mm PS gs":200, "Bolts":2},
                       "Bulbex Cable Cutter":{"Pliers Elite":1, "Nippers":1, "Toolset":1, "WD-40 (100ml)":2, "Metal Spare Parts":5, "Flat Screwdriver (Long)":1},
                       ".366 TKM AP-M":{"Pliers":1, "9x39mm SP-6 gs":50, "7.62x39mm PS gzh":100, "Gunpowder\"Kite\"":1},
                       "FLIR RS-32 2.25-9x 35mm 60Hz thermal riflescope":{"Tech Manual":1, "Toolset":1, "NIXXOR Lens":3, "Iridium Military Thermal Vision Module":2, "Virtex Programmable Processor":1, "SAS Drive":2, "Portable Powerbank":1},
                       "9x39mm SP-6 gs":{"Toolset":1, "7.62x39mm HP":120, "Gunpowder \"Eagle\"":2 , "Xenomorph Sealing Foam":2},
                       "9x19mm AP 6.3":{"Toolset":1, "9x19mm Pst Gzh":400, "Gunpowder \"Hawk\"":2},
                       "7.62x54mm R SNB gzh":{"Leatherman Multitool":1, "Gunpowder \"Hawk\"":1},
                       "5.56x45mm M856A1":{"Nippers":1, "5.56x45mm M855":200, "Gunpowder \"Hawk\"":2},
                       "Can of Thermite":{"Metal Cutting Scissors":1, "Set of Files \"Master\"":1, "Dorm Room 308 Key":1, "Gunpowder \"Kite\"":1, "Metal Spare Parts":1},
                       ".45 ACP AP":{"Set of Files \"Master\"":1, "Leatherman Multitool":1, ".45 ACP Lasermatch FMJ":120, "Gunpowder \"Hawk\"":1, "Gunpowder \"Eagle\"":1, "Pack of Nails":1} }

workbench_3_recipes = {"23x75mm \"Zvezda\" flashbang round":{"Leatherman Multitool":1, "Toolset":1, "Gunpowder \"Eagle\"":1, "SurvL Survival Lighter":5, "Gunpowder \"Kite\"":1, "\"Zarya\" stun grenade":1 },
                       "12/70 AP-20 armor-piercing slug":{"Flat Scredriver (Long)":1, "Nippers":1, "Gunpowder \"Hawk\"":1, "Damaged Hard Drive":1},
                       "5.56x45mm Warmageddon":{"Pliers Elite":1, "Gunpowder \"Kite\"":4, "Gunpowder \"Eagle\"":2},
                       "RGD-5 hand grenade":{"UZRGM Grenade Fuze":3, "TP-200 TNT Brick":2},
                       "9x19mm RIP":{"Nippers":1, "Gunpowder \"Hawk\"":1, "Bundle of Wires":4},
                       "9x39mm BP gs":{"Gunpowder\"Hawk\"":2, "Military Power Filter":2 },
                       "9x39mm SPP gs":{"Nippers":1, "9x21mm BT gzh":150, "Gunpowder \"Kite\"":2},
                       "OFZ 30x160mm shell":{"Pliers Elite":1, "Gunpowder \"Hawk\"":2, "Gunpowder \"Eagle\"":1, "TP-200 TNT Brick":2, "Can of Thermite":1 },
                       "9x19mm PBP gzh":{"Toolset":1, "Gunpowder \"Eagle\"":3, "Gunpowder \"Kite\"":4, "Can of Thermite":1, "Pack Of Nails":4},
                       "5.56x45mm M995":{"Leatherman Multitool":1, "Toolset":1, "Gunpowder \"Eagle\"":1, "OFZ 30x160mm Shell":2, "Can of Thermite":1},
                       "7.62x51mm M61":{"Leatherman Multitool":1, "Gunpowder \"Hawk\"":6, "Radiator Helix":3},
                       "7.62x39mm BP gzh":{"Leatherman Multitool":1, "Gunpowder \"Eagle\"":2, "Gunpowder \"Kite\"":2},
                       "5.45x39mm PPBS gs \"Igolnik\"":{"Pliers":1, "Nippers":1, "Gunpowder \"Kite\"":2, "Gunpowder \"Eagle\"":2, "Gunpowder \"Hawk\"":2},
                       "12.7x55mm PS12B":{"Set of files \"Master\"":1, "Bulbex Cable Cutter":1, "Military Cable":2, "TP-200 TNT Brick":2, "12.7x55mm PS12A":80},
                       "Weapon Repair Kit":{"Toolset":1, "Leatherman Multitool":1, "FireKlean Gun Lube":1, "Weapon Parts":10, "Insulating Tape":5, "Set of Files \"Master\"":1} }

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#nutrition
 
nutrition_1_recipes = {"Iskra Ration Pack":{"Army Crackers":1, "Can of Beef Stew (Small)":1, "Can of Squash Spread":1},
                       "Bottle of \"Norvinskiy Yadreniy\" premium kvass (0.6L)":{"Emelya Rye Croutons":4, "Bottle of Water (0.6L)":2},
                       "Can of Beef Stew (Small)":{"Can of Beef Stew (Large)":1, "Can of Squash Spread":1, "Rye Croutons":1},
                       "Can of Max Energy energy drink":{"BakeEzy Cook Book":1, "Can of TarCola Soda":1, "Can of Majaica Coffee Beans":1, "Bottle of Water (0.6L)":1},
                       "Emergency Water Ration":{"Silicone Tube":1, "Bottle of Water (0.6L)":1, "KEKTAPE Duct Tape":1} }

nutrition_2_recipes = {"Slickers Chocolate Bar":{"Alyonka Chocolate Bar":1, "Pack of Oat Flakes":1, "Army Crackers":1},
                       "Can of Condensed Milk":{"Pack of Milk":1, "Pack of Sugar":1},
                       "Pack of Sugar":{"Alyonka Chocolate Bar":2},
                       "Wilston Cigarettes":{"42 Signature Blend English Tea":1, "Apollo Soyuz Cigarettes":1},
                       "Aquamari Water Bottle with Filter":{"Water Filter":1, "Gas Mask Air Filter":1, "Bottle of Water (0.6L)":1, "Bottle of OLOLO Multivitamins":1},
                       "Can of Majaica Coffee Beans":{"Gunpowder \"Kite\"":1, "Can of Dr. Lupo's Coffee Beans":1} }

nutrition_3_recipes = {"Bottle of Tarkovskaya Vodka":{"Bottle of Water (0.6L)":5, "\"Fierce Hatchling\" Moonshine":1},
                       "Bottle of Dan Jackiel Whiskey":{"Water Filter":1, "Bottle of Water (0.6L)":2, "Bottle of Tarkovskaya Vodka":2, "Alyonka Chocolate Bar":1, "42 Signature Blend English Tea":1},
                       "Bottle of Water (0.6L)":{"Silicone Tube":1, "Canister with Purified Water":1},
                       "Bottle of \"Pevko Light\" Beer":{"Rye Croutons":5, "Bottle of \"Norvinskiy Yadreniy\" premium kvass (0.6L)":3, "Canister with Purified Water":1},
                       "Can of Hot Rod Energy Drink":{"BakeEzy Cook Book":1, "Water Filter":1, "Canister with Purified Water":1, "Pack of Sugar":1, "Can of Majaica Coffee Beans":1, "42 Signature Blend English Tea":1} }

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#intel

intel_2_recipes = {"Secure Flash Drive":{"Broken GPhone smartphone":1, "Broken GPhone X smartphone":1, "SSD Drive":1},
                   "Virtex Programmable Processor":{"Tech Manual":1, "Leatherman Multitool":1, "Military circuit board":2, "PC CPU":2, "Capacitors":5},
                   "Military COFDM Wireless Signal Transmitter":{"Toolset":1, "Tech Manual":1, "Broken GPhone X smartphone":1, "Portable Powerbank":1, "Military Circuit Board":1},
                   "VPX Flash Storage Module":{"Toolset":1, "RAM":3, "SSD Drive":2, "Broken GPhone Smartphone":3},
                   "UHF RFID Reader":{"Signal Jammer":1, "TerraGroup Labs Access Keycard":1, "VPX Flash Storage Module":1},
                   "Object #11SR keycard":{"VPX Flash Storage Module":1, "UHF RFID Reader":1, "Secure Flash Drive":5, "Object #21WS Keycard":1, "Secured Magnetic Tape Cassette":1},
                   "Topographic survey maps":{"Shoreline Plan Map":1, "Factory Plan Map":1, "Woods Plan Map":1, "Shoreline Health Resort Plan Map":1, "Customs Plan Map":1,  "Interchange Plan Map":1, "Secure Flash Drive":2},
                   "Military Flash Drive":{"Virtex Programmable Processor":1, "Secure Flash Drive":2, "Topographic Survey Maps":2} }

intel_3_recipes = {"Intelligence Folder":{"Printer Paper":1, "Military Flash Drive":2},
                   "Graphics Card":{"Tech Manual":1, "Ratchet Wrench":1, "Printed Circuit Board":10, "PC CPU":10, "CPU Fan":2, "VPX Flash Storage Module":3},
                   "TerraGroup Labs Keycard (Violet)":{"UHF RFID Reader":1, "TerraGroup Labs Access Keycard":12, "TerraGroup Labs Access Keycard (Yellow)":3, "Intelligence Folder":4, "Secure Magnetic Tape Cassette":1} }

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#medstation

medstation_1_recipes = {"AI-2 medkit":{"Pile of Meds":1},
                        "CALOK-B hemostatic applicator":{"Pile of Meds":1, "CALOK-B hemostatic applicator":1},
                        "Salewa first aid kit":{"Esmarch Tourniquet":2, "Car First Aid Kit":2},
                        "CMS surgical kit":{"Car First Aid Kit":1, "Medical Tools":1} }

medstation_2_recipes = {"Medical bloodset":{"Disposable Syringe":2, "Silicone Tube":1},
                        "Pile of meds":{"AI-2 Medkit":1, "Aseptic Bandage":1, "Augmentin Antibiotic Pills":1},
                        "IFAK individual first aid kit":{"Pile of Meds":2, "Army Bandage":2, "Esmarch Tourniquet":1},
                        "xTG-12 antidote injector":{"Adrenaline Injector":1, "AI-2 Medkit":2, "Pile of Meds":2},
                        "Morphine Injector":{"Pile of Meds":1, "Analgin Painkillers":1, "Disposable Syringe":1},
                        "SJ1 TGLabs combat stimulant injector":{"Pile of Meds":7, "Bottle of Saline Solution":2, "Propital Regenerative Stimulant Injector":3, "Morphine Injector":1},
                        "M.U.L.E. stimulant injector":{"Zagustin hemostatic drug injector":1, "Morphine Injector":1, "Can of Max Energy energy drink":2, "Pile of Meds":2},
                        "Portable defibrillator":{"Toolset":1, "Magnet":2, "Bundle of Wires":3, "Capacitors":4, "Portable Powerbank":1} }

medstation_3_recipes = {"Vaseline balm":{"Soap":3, "Schaman Shampoo":2, "Pile of Meds":1},
                        "AFAK tactical individual first aid kit":{"IFAK Individual First Aid Kit":2, "Army Bandage":1, "CAT Hemostatic Tourniquet":1},
                        "Grizzly medical kit":{"Pile of Meds":4, "CAT Hemostatic Tourniquet":2, "Aluminum Splint":1},
                        "Surv12 field surgical kit":{"Pile of Meds":6, "Medical Tools":2, "Esmarch Tourniquet":1},
                        "SJ6 TGLabs combat stimulant injector":{"SJ1 TGLabs combat stimulant injector":1, "Pile of Meds":2, "Bottle of Saline Solution":1, "Bottle of OLOLO Multivitamins":1},
                        "Propital regenerative stimulant injector":{"Ibuprofen Painkillers":1, "Golden Star Balm":1, "Pile of Meds":2},
                        "LEDX Skin Transilluminator":{"Toolset":1, "Ophthalmoscope":2, "Magnet":3, "UHF RFID Reader":3, "Portable Powerbank":3, "Portable Defibrillator":2} }
 
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#all

all_recipes = {"Workbench":[workbench_1_recipes, workbench_2_recipes, workbench_3_recipes],
               "Nutrition":[nutrition_1_recipes, nutrition_2_recipes, nutrition_3_recipes],
               "Intel":[intel_2_recipes, intel_3_recipes],
               "Medstation":[medstation_1_recipes, medstation_2_recipes, medstation_3_recipes]} 

keys = all_recipes.keys()
values = list(all_recipes.values())
keys, values = all_recipes.items()
 
