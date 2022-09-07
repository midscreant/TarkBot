# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 14:57:49 2022

@author: vinch
"""

#WEB SCRIPT

# import urllib.request

# desktop_path= "C:/Users/vinch/Desktop"
# og_url = "https://escapefromtarkov.fandom.com"
# item_list = ["/wiki/Broken_LCD", 
#  "/wiki/Printed_circuit_board", 
#  "/wiki/Power_cord", 
#  "/wiki/Gunpowder_%22Hawk%22", 
#  "/wiki/Magnet", 
#  "/wiki/Gas_analyzer", 
#  "/wiki/Printed_circuit_board", 
#  "/wiki/Weapon_parts", 
#  "/wiki/T-Shaped_plug", 
#  "/wiki/Weapon_parts", 
#  "/wiki/Kalashnikov_AK-74N_5.45x39_assault_rifle",  
#  "/wiki/Kalashnikov_AKM_7.62x39_assault_rifle", 
#  "/wiki/Gunpowder_%22Kite%22", 
#  "/wiki/12/70_8.5mm_Magnum_buckshot", 
#  "/wiki/Broken_GPhone_smartphone", 
#  "/wiki/VOG-25_Khattabka_improvised_hand_grenade", 
#  "/wiki/9x18mm_PM_RG028_gzh", 
#  "/wiki/Bundle_of_wires", 
#  "/wiki/Capacitors", 
#  "/wiki/Broken_GPhone_smartphone", 
#  "/wiki/PP-9_%22Klin%22_9x18PMM_submachine_gun", 
#  "/wiki/Round_pliers", 
#  "/wiki/Rechargeable_battery", 
#  "/wiki/GreenBat_lithium_battery", 
#  "/wiki/%22Zarya%22_stun_grenade", 
#  "/wiki/Electric_motor", 
#  "/wiki/Kalashnikov_AK-74M_5.45x39_assault_rifle", 
#  "/wiki/Geiger-Muller_counter", 
#  "/wiki/Gunpowder_%22Eagle%22", 
#  "/wiki/Gunpowder_%22Hawk%22", 
#  "/wiki/Spark_plug", 
#  "/wiki/12/70_flechette", 
#  "/wiki/Military_circuit_board", 
#  "/wiki/NIXXOR_lens", 
#  "/wiki/Car_battery", 
#  "/wiki/9x18mm_PM_PBM_gzh", 
#  "/wiki/12/70_SuperFormance_HP_slug", 
#  "/wiki/5.45x39mm_PP_gs", 
#  "/wiki/Bulbex_cable_cutter", 
#  "/wiki/.366_TKM_AP-M", 
#  "/wiki/FLIR_RS-32_2.25-9x_35mm_60Hz_thermal_riflescope", 
#  "/wiki/9x39mm_SP-6_gs", 
#  "/wiki/9x19mm_AP_6.3", 
#  "/wiki/7.62x54mm_R_SNB_gzh", 
#  "/wiki/5.56x45mm_M856A1", 
#  "/wiki/Can_of_thermite", 
#  "/wiki/.45_ACP_AP", 
#  "/wiki/23x75mm_%22Zvezda%22_flashbang_round", 
#  "/wiki/12/70_AP-20_armor-piercing_slug", 
#  "/wiki/5.56x45mm_Warmageddon", 
#  "/wiki/RGD-5_hand_grenade", 
#  "/wiki/9x19mm_RIP", 
#  "/wiki/9x39mm_BP_gs", 
#  "/wiki/9x39mm_SPP_gs", 
#  "/wiki/OFZ_30x160mm_shell", 
#  "/wiki/9x19mm_PBP_gzh", 
#  "/wiki/5.56x45mm_M995", 
#  "/wiki/7.62x51mm_M61", 
#  "/wiki/7.62x39mm_BP_gzh", 
#  "/wiki/5.45x39mm_PPBS_gs_%22Igolnik%22", 
#  "/wiki/12.7x55mm_PS12B"] 


# html_dict = {} 

# for item in item_list:
    
    
#     new_url = og_url + item
#     _list = new_url.split('/') 
#     name = _list[-1] 
    
#     fp = urllib.request.urlopen(new_url)
#     mybytes = fp.read() 
#     mystr = mybytes.decode("utf8")
#     fp.close()
#     html_dict[name] = mystr
    
#     print(name + " added") 

# with open(desktop_path + "/recipe_html_file.txt", 'w', encoding='utf-8') as file:
#     for name, html_content in html_dict.items():
#         print(name + ' testing')
#         print(type(html_content))
#         file.write(name)
#         file.write("\n\n")
#         file.write(str(html_content))

# print('success')   

# tr_dict = {}

# for name, html_content in html_dict.items():
#     _list = html_content.split(">")
#     for i in range(len(_list)):
#         _list[i] = _list[i] + ">"
#     i = 0
#     for line in _list:
#         _i = 1
#         endex = 0
#         if "<tr>" in line: 
#             new_list = _list[i:-1]
#             for item in new_list:
#                 if "</tr>" in item:
#                     endex = _i + i
#                 _i += 1
#             if name in tr_dict:
#                 tr_dict[name].append(_list[i:endex])
#                 print('adding to ' + name + " entry...")
#             else:
#                 tr_dict[name] = [_list[i:endex]]
#                 print("creating " + name + " entry...")
#         i += 1 
        
# with open(desktop_path + "/recipe_trs.txt", "w", encoding="utf-8") as file:
#     for name, html_content in tr_dict.items():
#         print(name + ' testing') 
#         file.write(name)
#         file.write("\n\n")
#         file.write(str(html_content))

# tr_keys = tr_dict.keys()
# print(tr_keys)
# tr_values = list(tr_dict.values())
# print(type(tr_values)) 
# print(tr_values[:3])

# for name, html_content in tr_dict.items():
    #html_content is a list of a list
    # titles = []
    # ingredients = {}
    
    # for _list in html_content:
    #     if "title=" in 
        
from recipes___ import all_recipes

print(all_recipes["Intel"])      
                   
    
 