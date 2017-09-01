def dictionary(string):
    d = dict(string.split('=') for string in string.split(';'))
    return d
string = raw_input("Enter the string: ")
dictionary(string)
string2 = dictionary(string)
print string2
    
    

    
