# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:05:18 2018

@author: Bradyjomark
"""
def core():
    operation = input("Enter an operation : ")
    if operation == 'end':
        print("Program closed")
    
    elif operation == 'info':
        print("Possible operations are : (I don't have any yet)")
        return core()
    else:
        print(str(operation) + " is sadly not supported by my program" + '\n' + 'type "info" to know all the supported programs')
        return core()

core()