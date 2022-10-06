# -*- coding: utf-8 -*-

#ERROR CHECKING

class ErrorChecker:
    
    def tryFunction(self, function, *arguments):
        status = None
        status = function(*arguments)
        return status
    
    def errorChecker(self, function, *arguments):
        for i in range(3):
            status = None
            if len(arguments) > 0 and arguments != ():
                status = self.tryFunction(function, *arguments)
            else:
                status = self.tryFunction(function)
            if status == 'fail':
                continue
            elif status == "FATAL":
                return "FATAL"
            elif status == "buy_fail":
                return "buy_fail"
            else:
                return
        print("Function still failing after 3 attempts...")
        return 'fail'