import sys
import re

def read_files(file_path):

    # This is will make sure the things we pass in are files, if not an error  will be thrown 
    try:
        # This reads the file and returns the file.
        with open(file_path, 'r') as file:
            content = file.read()
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
    list_1 = set(file_into_a_list(txt1))
    list_2 = set(file_into_a_list(txt2))

    # Creates a list that is sorted, and in difference
    difference_result = sorted(list(list_1.difference(list_2)))

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
    list_1 = set(file_into_a_list(txt1))
    list_2 = set(file_into_a_list(txt2))


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
    list_1 = set(file_into_a_list(txt1))
    list_2 = set(file_into_a_list(txt2))

    print(list_1)
    print(list_2)

'''
    # This is where the actual intersection takes places but the value is in a set
    intersection_result = sorted(list(list_1.intersection(list_2)))
    
    # This writes the word into the result txt file.
    result_file = 'result.txt'
    with open(result_file, 'w') as result_file:
        for x in range(len(intersection_result)):
            if x == len(intersection_result) - 1:
                result_file.write(intersection_result[x])
            else:
                result_file.write(intersection_result[x]+ '\n')
            
    result_file.close()
'''


    
# This converts the txt file into a list.
def file_into_a_list(txt):
    try:
        with open(txt, 'r') as file:
            # Reads each line in the file, and withing each line it will read each word and split \.(?!d) -> all . that have zero to one occurences of no digits after it
            # |[\s,]+ -> OR split according to white space, and comma. And return that. ***
            words = [word.strip().lower() for line in file for word in re.split(r'\.(?!\d)|[\s,+-=/]+', line) if word]
            return words
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






