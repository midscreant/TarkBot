# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:50:30 2022

@author: vinch
"""

#2ndd take at error checker


class ErrorChecker:
    
    def tryFunction(self, function, *arguments):
    # try:
        empty_tuple = ()
        status = None
        # print("Args " + str(*arguments))
        # if len(arguments) > 0 and arguments != empty_tuple:
        #     status = function(*arguments)
        # else:
        status = function(*arguments)
        if status == "fail":
            return "fail"
        elif status == "FATAL":
            return "FATAL"
        # except:
        #     print("Fatal error while running " + str(function))
        #     return "fail"
    
    def errorChecker(self, function, *arguments):
        # print("Args 2 " + str(*arguments))
        empty_tuple = ()
        for i in range(3):
            status = None
            if len(arguments) > 0 and arguments != empty_tuple:
                status = self.tryFunction(function, *arguments)
            else:
                status = self.tryFunction(function)
            if status == 'fail':
                continue
            elif status == "FATAL":
                return "FATAL"
            else:
                return
        print("Function still failing after 3 attempts...")
        return 'fail'
                