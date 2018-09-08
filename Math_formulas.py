# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 19:18:26 2018

@author: Bradyjomark
"""

def area_of_a_parallelogram():
    """
    Prints the missing variable in the parallelogram
    
    The user inputs should be two ints or floats and one ?
    """
    while True:
        
        A = input("Enter the Area ")
        b = input("Enter the Base ")
        h = input("Enter the Height ")
        if A == '?':
            print('The Area is : ' + str(int(b)*int(h)))
            break
        
        elif b == '?':
            print('The Base is : ' + str(int(A)/int(h)))
            break
        elif h == '?':
            print('The Height is : ' + str(int(A)/int(b)))
            break
        
        else:
            print('You did not enter two ints/floats and a \'?\'')