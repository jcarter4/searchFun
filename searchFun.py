import time
import logging
from os import system

###########################################################################################################
#  Author: Johnny Carter                                                                                  #
#  Version: 1.0.1                                                                                         #
#  Brief Description: This program is for searching integer lists for certain integers, each function is  #
#  callable when the script is imported by another script.                                                #
###########################################################################################################



###########################################################################################################
#                             start the main function                                                     #
###########################################################################################################
def search_input(logging_level=0 , search_method=0 , target=int, list=int):

    #We want to log the process
    
    if logging_level == 1:
        logging.basicConfig(filename="binarySearch.log", level=logging.INFO)
        logging.info('Started logs..')

        if search_method == 0: # linear search
            print(lineSearch(list, target))
    
        elif search_method == 1: # binary search
            print(binaSearch_ascend(list, target))
        
        elif search_method == 2: # binary seach descending order
            print(binaSearch_descend(list, target))

        else:
            print(f"Invalid option selected {search_method} is not an option")
    
    # we don't want logging

    else:
        if search_method == 0: # linear search
            print(lineSearch(list, target))
    
        elif search_method == 1: # binary search ascending order
            print(binaSearch_ascend(list, target))
        
        elif search_method == 2: # binary seach descending order
            print(binaSearch_descend(list, target))
        
        else:
            print(f"Invalid option selected {search_method} is not an option")    



###########################################################################################################
#                    if method is defined as binary(ascending) start this function                        #
###########################################################################################################
def binaSearch_ascend(input, target):
    
    #set the variables
    target = int(target)
    start = time.perf_counter()
    first = 0
    last = len(input) -1
    index = -1
    logging.info("searching...")

    # run a while loop as long as we haven't searched everything
    while (first <= last) and (index == -1):
        mid = (first+last) // 2 # this is more effective than last - first 
        logging.info(f"New Target {mid}")

        if input[mid] != target and first == last:
            logging.error(f'{target} not found in list')
            raise ValueError(f'{target} not found in list')

        #if we find the value break the while loop
        if input[mid] == target:
            index = mid
            logging.info(f"Target Found at {index}")

        # if the value isn't equal to target then adjust search parameters    
        else:
    
            if target < input[mid]:
                last = mid - 1
                logging.info("Too High")
    
            else:
                first = mid + 1
                logging.info("Too Low")

    end = time.perf_counter()

    logging.info(f"time was {end - start} seconds")

    return mid



###########################################################################################################
#                    if method is defined as binary(descending) start this function                       #
###########################################################################################################
def binaSearch_descend(input, target):
    
    #set the variables
    target = int(target)
    start = time.perf_counter()
    first = 0
    last = len(input) -1
    index = -1
    logging.info("searching...")

   
    # run a while loop as long as we haven't searched everything
    while (first <= last) and (index == -1):
        

        mid = (first+last) // 2    # this is more effective than last - first 
        logging.info(f"New Target {mid}")

        if input[mid] != target and first == last:
            logging.info(f'{target} not found in list')
            raise ValueError(f'{target} not found in list')

        #if we find the value break the while loop
        if input[mid] == target:
            index = mid
            logging.info(f"Target Found at {index}")

        # if the value isn't equal to target then adjust search parameters    
        else:
    
            if target > input[mid]:
                last = mid - 1
                logging.info("Too High")
    
            else:
                first = mid + 1
                logging.info("Too Low")

    end = time.perf_counter()

    logging.info(f"time was {end - start} seconds")

    return mid


###########################################################################################################
#                    if method is defined as linear start this function                                   #
###########################################################################################################
def lineSearch(input, target):
    
    start = time.perf_counter()

    for newTarget in range(len(input)):
    
        # print(newTarget)
        if input[newTarget] == target:
            logging.info(f"Target Found at {newTarget}")
            end = time.perf_counter()
            logging.info(f"time was {end - start} seconds")
    
            return newTarget

    return -1



def user_Input_Valdiation():
    pass


###########################################################################################################
#                    Testing for the functions in this program                                            #
###########################################################################################################
if __name__ == '__main__':

    #static variable for a list to search through
    lyst = list(range(0, 10000000))

    #get the input for the search from user
    try:
        target = (input("What is your target?"))
        targetNum = int(target)
    
    except ValueError as valErr:
        system('clear')
        print(f"{target} is not a valid target\n Ending program.")      
        time.sleep(2)
        



    #Request search method from user
    try:

        search_method_in = (input("What method would you like to use?\n0(linear search)\n1(binary search)\n:"))
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