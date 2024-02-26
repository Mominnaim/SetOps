import sys


def getWords(txt):

    word = []
    return mergeSort(removeDuplicates(parseWords(word,open(txt, "r").read(),0),0))

"""
    words3 = union(words, words2)
    words3 = intersection(words, words2, 0)
    #words3 = difference(words, words2, 0)
    #words3 = mergeSort(words3)
    return words3
"""

# The starting point for the actual remove function which is called removeDupHelp()
def removeDuplicates(wordsList, index):

    # the base case
    if index + 1 >= len(wordsList):
        return wordsList
    
    # Otherwise come here and go to the acutal remove duplicate function
    else:
        # Update wordsList with the result of removeDupHelp
        #wordsList = removeDupHelp(wordsList, index + 1, wordsList[index])
        # Recur for the next word

        return removeDuplicates(removeDupHelp(wordsList, index + 1, wordsList[index]), index + 1)

# This is the actual function where the duplicates get deleted
def removeDupHelp(wordsList, index, target):

    # This is the base case for this function
    if index > len(wordsList) - 1:
        return wordsList
    
    # elif the word matches the target then  append everything 
    elif wordsList[index] == target:

        # wordsList = wordsList[:index] + wordsList[index + 1:]
        # Recur for the same index as the length has reduced after removal

        return removeDupHelp(wordsList[:index] + wordsList[index + 1:], index, target)
    else:
        # Recur for the next character
        return removeDupHelp(wordsList, index + 1, target)
    

def intersection(wordsList1, wordsList2, index):
    if index > len(wordsList1)-1:
        if len(wordsList1) == 0:
            return []
        else:
            return_result_file(wordsList1)
    else:
        if (removeIntersectionHelp(wordsList2, 0, wordsList1[index])): 
            return intersection(wordsList1, wordsList2, index + 1)
        
        else:
            #wordsList1 = wordsList1[:index] + wordsList1[index + 1:]
            return intersection(wordsList1[:index] + wordsList1[index + 1:], wordsList2, index)
        # Recur for the next word
            
def removeIntersectionHelp(wordsList, index, target):
    if index > len(wordsList) - 1:
        return False
    elif wordsList[index] == target:
        return True
    else:
        # Recur for the next character
        return removeIntersectionHelp(wordsList, index + 1, target)


def difference(wordsList1, wordsList2, index):
    if index >= len(wordsList1): 
         return_result_file(wordsList1)
    else:
        if (removeDifferenceHelp(wordsList2, 0, wordsList1[index])): # -----------> (x,y,z) where x is the #2 list that is being checked, y = is the index, and z is the target word from the from list #1
            return difference(wordsList1, wordsList2, index + 1) # ------------> This is the recursion where it adds one to the index and repeats.
        
        else:
            #wordsList1 = wordsList1[:index] + wordsList1[index + 1:]
            return difference(wordsList1[:index] + wordsList1[index + 1:], wordsList2, index) # ----------> It will first check the if, and if it doesnt return true, then it will come here.
        # Recur for the next word
            
def removeDifferenceHelp(wordsList, index, target):
    if index > len(wordsList) - 1:
        return True
    elif wordsList[index] == target:
        return False
    else:
        # Recur for the next element
        return removeDifferenceHelp(wordsList, index + 1, target)
    

def union(wordsList1, wordsList2): 
    return_result_file(mergeSort(removeDuplicates(wordsList1 + wordsList2, 0)))


def parseWords(wordsList, line, index):
    while index < len(line):
        if (line[index] in '0123456789'):
            index += 1
        elif (line[index] in 'abcdefghijklmnopqrstuvwxyz'):
            index += 1
        elif (line[index] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            #lowercaseChar = chr(ord(line[index]) + 32)
            line = line[:index] + chr(ord(line[index]) + 32) + line[index + 1:]
            index += 1
        else:
            if (line[index] == "."):
                if index != 0:
                    if (index != len(line) - 1):
                        if (line[index-1] in '0123456789'): # -------------------------- To check if the index after is a number
                            if (line[index+1] in '012345679'): # -------------------------- To check if the index before is a number
                                    index += 1 
                            else:                              # -------------------------- If no number in front of the period then append the word
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
    return wordsList


def mergeSort(arr):
    #n = len(arr)
    if len(arr) <= 1:
        return arr
    else:

        return merged(mergeSort(arr[0:(len(arr) // 2)]),mergeSort(arr[(len(arr) // 2):len(arr)]),0,0)
    
def merged(left,right,i,j):
    mergedArray = []
    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            mergedArray.append(left[i])
            i += 1
        else:
            mergedArray.append(right[j])
            j += 1
    mergedArray.extend(left[i:])
    mergedArray.extend(right[j:])
    return mergedArray


def perform_operation(txt1, txt2, operation):

    # If difference operation is selected
    if operation == 'difference':
        difference(txt1, txt2,0)

    # If union operator is selected
    elif operation == 'union':
        union(txt1, txt2)

    # If intersection is selected intersection
    elif operation == 'intersection':
        intersection(txt1, txt2,0)

    else:
        print("sorry but that is not a valid operation.")
        sys.exit(1)

def return_result_file(txt_list):
    with open('result.txt', 'w') as result_file:
        result_file.write('\n'.join(txt_list))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Format: python setops.py \"set1=[filename]; set2=[filename];operation=[difference|union|intersection]\"")
        sys.exit(1)

    # argv[1] is the string of set1, set2, and operation and its splits it with semi colon
    args = sys.argv[1].split(';')

    # There are three elements now which each one of them being assigned a variable.
    #set1 = getWords(args[0].split('=')[1])
    #set2 = getWords(args[1].split('=')[1])
    #operation = args[2].split('=')[1]

    perform_operation(getWords(args[0].split('=')[1]), getWords(args[1].split('=')[1]), args[2].split('=')[1])


    # If the correct parameters are passed in then start the actually part of the code.
    # perform_operation(set1, set2, operation)