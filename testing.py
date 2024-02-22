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
numbers = r'1234567890'



def file_into_a_list(txt):
    funnel_list = []

    main_list = []

    result = ''.join(char for char in txt)
    for x in range(len(result)):
        if result[x] in skip:
            continue
        elif result[x] in seperator_1:
            if result[x] == '.':
                if result[x + 1] in numbers:
                    funnel_list.append(result[x])
            else:
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
                

    lowercased_list = [item.lower() if isinstance(item, str) else item for item in main_list]
    print(lowercased_list)


testing = 'tree, 12.34 Blue. 56.78 hot. 91011 rock 12.13 star 91011 Moon. 91.012'

file_into_a_list(testing)