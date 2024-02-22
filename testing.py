import re
"""
def file_into_a_list(txt):
    try:
        with open(txt, 'r') as file:
            # Reads each line in the file, and withing each line it will read each word and split \.(?!d) -> all . that have zero to one occurences of no digits after it
            # |[\s,]+ -> OR split according to white space, and comma. And return that. ***
            words = [word.strip().lower() for line in file for word in re.split(r'\.(?!\d)|[\s,+-=/]+', line) if word]
            print(words)

    except FileNotFoundError:
        print(f"Error: File '{txt}' not found.")
        return []
    
"""

skip = r'!@#$%^?&<>`~;:'
seperator_1 = r'. +-=/'



def file_into_a_list(txt):
    funnel_list = []

    main_list = []

    result = ''.join(char for char in txt)
    for x in range(len(result)):
        if result[x] in skip:
            continue
        elif result[x] in seperator_1:
            if len(funnel_list) != 0:
                new_word = ''.join(char for char in funnel_list)
                main_list.append(new_word)
                funnel_list = []
            else:
                continue

        else:
            if x == len(result) - 1:
                funnel_list.append(result[x])
                new_word = ''.join(char for char in funnel_list)
                main_list.append(new_word)
                funnel_list = []
            else:
                funnel_list.append(result[x])
                


    print(main_list)


testing = '#hell.o an%d w3lco+me t^e>s<t&i!n?g'

file_into_a_list(testing)