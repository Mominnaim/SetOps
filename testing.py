import re
"""


def file_into_a_list(txt):

    skip = r'!@#$%^?&<>`~;:'
    seperator_1 = r'. +-=/,' + '\n'
    numbers = r'1234567890'

    funnel_list = []

    main_list = []

    result = ''.join(char for char in txt)
    print(result)

    # This is the for loop that itterates over each character in result 
    for x in range(len(result)):
                
                #if the current index is a skip symbol, we just pass over it.
                if result[x] in skip:
                    continue

                # If the current index is a seperator symbol than we go into this elif
                elif result[x] in seperator_1:

                    # If the seperator is a . AND if the . is not the first thing in the list -> we go here
                    if result[x] == '.' and x != 0:
                        
                        # If the next index is a number and index before is also a number than we will append the . rather then splitting it.
                        if result[x + 1] in numbers and result[x-1] in numbers :
                            funnel_list.append(result[x])


                        # if the next index is NOT a number and the previous index IS a number -> we go here 
                        elif (result[x + 1] not in numbers and result[x-1] in numbers):

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
                

    lowercased_list = [item.lower() if isinstance(item, str) else item for item in main_list]
    print(lowercased_list)

testing = '1a1 tw0 1.a.1 #.1 1.a b.2 test.red'
testing_1 = '#hell.o an%d w3lco+me 4.14 4.a 1..2 t^e<s>t!i&ng a, , , a \n\n\n 33' 
file_into_a_list(testing)
file_into_a_list(testing_1)

"""

# wordlist is an empty list , line is the line that are being passed in through the file, index is 0 by defualt


def parseWords(wordsList, line, index):
    funnel_list = []
    while index < len(line):

        # If the current index is a number, then add one to the index
        if (line[index] in '0123456789'):
            index += 1

        # If the current index is a lowercase letter, then add one to the index    
        elif (line[index] in 'abcdefghijklmnopqrstuvwxyz'):
            index += 1
        # If the curren index is a upper case letter then, lowercase it then add one. 
        elif (line[index] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):

            # You just took that upper case letter and lowercased it, now to add it back in the string, you would split the string from 0 to the index + the lowercase letter + the index and on. 
            lowercaseChar = chr(ord(line[index]) + 32)
            line = line[:index] + lowercaseChar + line[index + 1:]
            index += 1

        # If it not a lowercase,uppercase, or number come here
        else:

            # If the current index is a . then come here
            if (line[index] == "."):

                # if the index is not 0 then we can move on since we know it is not the first thing in the list
                if index != 0:

                    if (index != len(line) - 1):
                        if (line[index-1] in '0123456789'): 
                            if (line[index+1] in '012345679'): # -------------------> If there is a number behind it and a number infront of it, then we can append the whole number.
                                    index += 1 

                            #         
                            else:                              
                                wordsList.append(line[:index])
                                line = line[index + 1:]
                                index = 0
                        else:
                            wordsList.append(line[:index])
                            line = line[index + 1:]
                            index = 0
                    else:
                        wordsList.append(line[:index])
                        line = line[index + 1:]
                        index = 0
                else:
                    line = line[index + 1:]
                    index = 0
            else:
                if index != 0:
                    wordsList.append(line[:index])
                line = line[index + 1:]
                index = 0
    if index != 0:
        wordsList.append(line)
    return (wordsList)


words = []
line = 'This is an example code a!1'

print(parseWords(words,line,0))