import sys
import re

def read_files(file_path):

    # This is will make sure the things we pass in are files, if not an error  will be thrown 
    try:
        # This reads the file and returns the file.
        with open(file_path, 'r') as file:
            content = file.read() # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
            return file_path
    # If the file is not found, then the error is printed
    except FileNotFoundError:
        print('The file has not been found')

# We will check what the operation is and from there we will go to the function according to that 
def perform_operation(txt1, txt2, operation):

    # If difference operation is selected
    if operation == 'difference':
        difference_function(txt1, txt2)

    # If union operator is selected
    elif operation == 'union':
        union_function(txt1, txt2)

    # If intersection is selected intersection
    elif operation == 'intersection':
        intersection_function(txt1, txt2)

    else:
        print("sorry but that is not a valid operation.")
        sys.exit(1)


# This is for the difference operater function
def difference_function(txt1, txt2):

    # This creates two variables using the same function to store the the list of each file.
    list_1 = set(file_into_a_list(txt1)) # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
    list_2 = set(file_into_a_list(txt2)) # --------------------------------------------------------------------------------->   YOU CANNOT HAVE

    # Creates a list that is sorted, and in difference
    difference_result = sorted(list(list_1.difference(list_2))) # --------------------------------------------------------------------------------->   YOU CANNOT HAVE

    # This writes the word into the result txt file.
    # Essentially what this does is create file name result.txt and for every x in the length of difference_result, write that word into the new file with \newLine 
    # UNLESS it is the last word then you can just write the word without the new line 

    result_file = 'result.txt'
    with open(result_file, 'w') as result_file:
        for x in range(len(difference_result)):
            if x == len(difference_result) - 1:
                result_file.write(difference_result[x])
            else:
                result_file.write(difference_result[x]+ '\n')
            
    result_file.close()


# This is for the union operater function
def union_function(txt1, txt2):

    # This creates two variables using the same function to store the the list of each file.
    list_1 = set(file_into_a_list(txt1)) # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
    list_2 = set(file_into_a_list(txt2)) # --------------------------------------------------------------------------------->   YOU CANNOT HAVE

    union_result = sorted(list(list_1.union(list_2)))
    
    # This writes the word into the result txt file.
    result_file = 'result.txt'
    with open(result_file, 'w') as result_file:
        for x in range(len(union_result)):
            if x == len(union_result) - 1:
                result_file.write(union_result[x])
            else:
                result_file.write(union_result[x]+ '\n')
            
    result_file.close()
    

# This is for the intersection operater function 
def intersection_function(txt1,txt2):

    # This creates two variables using the same function to store the the list of each file.
    list_1 = set(file_into_a_list(txt1)) # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
    list_2 = set(file_into_a_list(txt2)) # --------------------------------------------------------------------------------->   YOU CANNOT HAVE


    # This is where the actual intersection takes places but the value is in a set
    intersection_result = sorted(list(list_1.intersection(list_2))) # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
    
    # This writes the word into the result txt file.
    result_file = 'result.txt'
    with open(result_file, 'w') as result_file:
        for x in range(len(intersection_result)):
            if x == len(intersection_result) - 1:
                result_file.write(intersection_result[x])
            else:
                result_file.write(intersection_result[x]+ '\n')
            
    result_file.close()

    
# This converts the txt file into a list.
def file_into_a_list(txt):
    skip = r'!@#$%^?&<>`~;:' # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
    seperator_1 = r'. +-=/,*()' + '\n' + ' \'' + '\t' + '\r' # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
    numbers = r'1234567890' # --------------------------------------------------------------------------------->   YOU CANNOT HAVE

    funnel_list = [] # --------------------------------------------------------------------------------->   YOU CANNOT HAVE

    main_list = [] # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
    
    try:
        with open(txt, 'r') as file:
            result = ''.join(char for char in file)
            for x in range(len(result)):
            
                #if the current index is a skip symbol, we just pass over it.
                if result[x] in skip:
                    continue

                # If the current index is a seperator symbol than we go into this elif
                elif result[x] in seperator_1:

                    # If the seperator is a . AND if the . is not the first thing in the list -> we go here
                    if result[x] == '.' and x != 0 and x != len(result)-1 :
                        
                        # If the next index is a number and index before is also a number than we will append the . rather then splitting it.
                        if result[x + 1] in numbers and result[x-1] in numbers :
                            funnel_list.append(result[x])


                        # if the next index is NOT a number and the previous index IS a number -> we go here 
                        elif result[x + 1] not in numbers and result[x-1] in numbers:

                            # if there is nothing in the funnel list 
                            if len(funnel_list) == 0:
                                    continue
                            
                            # If there is something in the funnel list then push it to the main
                            else:
                                new_word = ''.join(char for char in funnel_list)
                                main_list.append(new_word)
                                funnel_list = []

                        # if the next index IS a number and the previous index is NOT a number than -> come here
                        elif result[x + 1] in numbers and result[x-1] not in numbers:

                            # if there is nothing in the funnel list 
                            if len(funnel_list) == 0:
                                    continue
                            
                            # If there is something in the funnel list, then push it to the main
                            else:
                                new_word = ''.join(char for char in funnel_list)
                                main_list.append(new_word)
                                funnel_list = []
                        
                        # If both the indexes front and back are not numbers the come here
                        elif result[x + 1] not in numbers and result[x-1] not in numbers:

                            # if there is nothing in the funnel list 
                            if len(funnel_list) == 0:
                                 continue
                            
                            # If there is something in the funnel list, then push it to the main
                            else:
                                new_word = ''.join(char for char in funnel_list)
                                main_list.append(new_word)
                                funnel_list = []
                        
                    # If the seperator is not a . -> then we will push whatever we have in the funnel into the main list.        
                    else:

                        # If there is something within the funnel list, it will be pushed into the main.
                        if len(funnel_list) != 0:
                            new_word = ''.join(char for char in funnel_list)
                            main_list.append(new_word)
                            funnel_list = []

                        # If there is nothing withing the funnel list you move on the next index
                        else:
                            continue

                # If the current index is a letter or number then we go into this if else statement 
                else:

                    # If the current index is the last index in the list, then we will push whatever we have in the funnel to the main.
                    if x == len(result) - 1:
                        funnel_list.append(result[x])
                        new_word = ''.join(char for char in funnel_list)
                        main_list.append(new_word)
                        funnel_list = []

                    # If there are more indexs then we come here
                    else:

                        # if the current index is NOT a number and the next index IS a number than append the current index, then push whatever is in the funnel to the main 
                        if (result[x] not in numbers and result[x+1] in numbers):
                            funnel_list.append(result[x])
                            new_word = ''.join(char for char in funnel_list)
                            main_list.append(new_word)
                            funnel_list = []

                        # if the current index IS a number and the next index is NOT a number than append the current index, then push whatever is in the funnel to the main 
                        elif (result[x] in numbers and result[x+1] not in numbers and result[x + 1] not in seperator_1):
                            funnel_list.append(result[x])
                            new_word = ''.join(char for char in funnel_list)
                            main_list.append(new_word)
                            funnel_list = []

                        # else just push the current index 
                        else:
                            funnel_list.append(result[x])
                

        lowercased_list = [item.lower() if isinstance(item, str) else item for item in main_list] # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
        return lowercased_list # --------------------------------------------------------------------------------->   YOU CANNOT HAVE
    except FileNotFoundError:
        print(f"Error: File '{txt}' not found.")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Format: python setops.py \"set1=[filename]; set2=[filename];operation=[difference|union|intersection]\"")
        sys.exit(1)

    # argv[1] is the string of set1, set2, and operation and its splits it with semi colon
    args = sys.argv[1].split(';')

    # There are three elements now which each one of them being assigned a variable.
    set1 = read_files(args[0].split('=')[1])
    set2 = read_files(args[1].split('=')[1])
    operation = args[2].split('=')[1]


    # If the correct parameters are passed in then start the actually part of the code.
    perform_operation(set1, set2, operation)
