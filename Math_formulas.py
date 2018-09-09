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
            print('The Area is : ' + str(float(b)*float(h)))
            return float(b)*float(h)
        
        elif b == '?':
            print('The Base is : ' + str(float(A)/float(h)))
            return float(A)/float(h)
        elif h == '?':
            print('The Height is : ' + str(float(A)/float(b)))
            return float(A)/float(b)
            
        
        else:
            print('You did not enter two ints/floats and a \'?\'')
            

def area_of_a_triangle():
    """
    Prints the missing variable in the triangle
    
    The user inputs should be two ints or floats and one ?
    """
    while True:
        
        A = input("Enter the Area ")
        b = input("Enter the Base ")
        h = input("Enter the Height ")
        if A == '?':
            print('The Area is : ' + str(float(b)*float(h)*0.5))
            return float(b)*float(h)*0.5
            
        
        elif b == '?':
            print('The Base is : ' + str(float(A)*2/float(h)))
            return float(A)*2/float(h)
            
        elif h == '?':
            print('The Height is : ' + str(float(A)*2/float(b)))
            return float(A)*2/float(b)
        
        else:
            print('You did not enter two ints/floats and a \'?\'')
