from Math_formulas import *

def core():
    operation = input("Enter an operation : ")
    if operation == 'end':
        print("Program closed")
    
    elif operation == 'info':
        print("Possible operations are : (area of a parallelogram, area of a triangle)")
        core()
    elif operation == 'area of a parallelogram':
        area_of_a_parallelogram()
        core()
    elif operation == 'area of a triangle':
        area_of_a_triangle()
        core()
    else:
        print(str(operation) + " is sadly not supported by my program" + '\n' + 'type "info" to know all the supported programs')
        core()

core()
