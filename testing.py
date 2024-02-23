import re
"""

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


                        # If the next index is not a number, we will take whatever we have in the funnel and push that to the main    
                        elif result[x + 1] not in numbers and result[x-1] in numbers:
                            if len(funnel_list) == 0:
                                 continue
                            else:
                                new_word = ''.join(char for char in funnel_list)
                                main_list.append(new_word)
                                funnel_list = []

                        elif result[x + 1] in numbers and result[x-1] not in numbers:
                            if len(funnel_list) == 0:
                                 continue
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

                        #
                        if (result[x] not in numbers and result[x+1] in numbers):
                            funnel_list.append(result[x])
                            new_word = ''.join(char for char in funnel_list)
                            main_list.append(new_word)
                            funnel_list = []

                        #
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

testing = '1a1 tw0 1.a.1 #.1 1.a b.2'
testing_1 = '#hell.o an%d w3lco+me 4.14 4.a 1..2 t^e<s>t!i&ng a, , , a \n\n\n 33' 
file_into_a_list(testing)
file_into_a_list(testing_1)