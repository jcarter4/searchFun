
from searchFun import *
from os import system

#static variable for a list to search through
lyst = list(range(0, 10000000, 10))

#get the input for the search from user
try:
    target = (input("What is your target?"))
    targetNum = int(target)

except ValueError as valErr:
    system('clear')
    print(f"{target} is not a valid target\n Ending program.")      
    time.sleep(2)
    
    raise ValueError(f"Input must be int your input was {type(target)}")



#Request search method from user
try:

    search_method_in = (input("What method would you like to use?\n0(linear search)\n1(binary search ascending)\n2(binary search descending):"))
    search_method = int(search_method_in)
    system('clear')
except ValueError as vErr:
    system('clear')
    print(f"{search_method_in} is not a valid target\n Ending program.")      
    time.sleep(2)
    
    raise ValueError(f"Input must be int your input was {type(target)}")

logging_level = int(input("select logging level:\n0 = no logging:\n1 = INFO level"))
system('clear')
    
search_input(logging_level, search_method, target, lyst)

