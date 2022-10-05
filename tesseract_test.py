# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:55:04 2022

@author: vinch
"""

# import inspect

# class Test:
#     def test(self):
#         def deeper():
#             print(inspect.stack()[0][3])
#         deeper()
    
# tester = Test()
# tester.test()


import pytesseract
from PIL import Image
import os

strip_var = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*)(}{-_=+><\\/?'\";:][.\n "

pytesseract.pytesseract.tesseract_cmd = r"C:/Users/vinch/miniconda3/Library/bin/tesseract"
tessdata_dir_config = '--tessdata-dir "C:/Users/vinch/miniconda3/share/tessdata"'

value = "\n"
print('a')
print(value.strip("\n"))
print('b')

os.chdir("C:/Users/vinch/Desktop/Photos")
print(pytesseract.image_to_string(Image.open(r'C:/Users/vinch/Desktop/Photos/test_6.png'), config=tessdata_dir_config).strip())
print(pytesseract.image_to_string(Image.open(r'C:/Users/vinch/Desktop/Photos/test_6.png'), config=tessdata_dir_config).strip(strip_var))
_str = pytesseract.image_to_string(Image.open(r'C:/Users/vinch/Desktop/Photos/test_6.png'), config=tessdata_dir_config).strip(strip_var)
_list = _str.split(" ")
print(_list)
stripped_list = []
for item in _list:
    stripped_list.append(item.strip(strip_var))
print(stripped_list)
int_list = []
for item in stripped_list:
    try:
        _int = int(item)
        int_list.append(_int)
    except:
        continue
print(int_list)
# if len(int_list) != 2:
#     print("fail")
#     return "FATAL"

purchased_amount = int_list[1]  

# return purchase_amount  


if "" == pytesseract.image_to_string(Image.open(r'C:/Users/vinch/Desktop/Photos/test_6.png'), config=tessdata_dir_config).strip():
    print("a")
print("-_-test---".strip("-_-"))
