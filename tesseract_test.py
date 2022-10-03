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

#TESSERACT PATH
    # + "\\pkgs



pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\vinch\\miniconda3\\Library\\bin\\tesseract"

os.chdir("C:/Users/vinch/Desktop/Photos")
print(pytesseract.image_to_string(Image.open(r'C:/Users/vinch/Desktop/Photos/tips_origins.png')))