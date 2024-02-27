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
    try:
    # the base case
        if index + 1 >= len(wordsList):
            return wordsList
        
        # Otherwise come here and go to the acutal remove duplicate function
        else:
            # Update wordsList with the result of removeDupHelp
            #wordsList = removeDupHelp(wordsList, index + 1, wordsList[index])
            # Recur for the next word
            return removeDuplicates(removeDupHelp(wordsList, index + 1, wordsList[index]), index + 1)
    except:
        return []

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
    if index >= len(wordsList1):
        return_result_file(wordsList1)
    else:
        if (removeIntersectionHelp(wordsList2, 0, wordsList1[index])): 
            return intersection(wordsList1, wordsList2, index + 1)
        
        else:
            #wordsList1 = wordsList1[:index] + wordsList1[index + 1:]
            return intersection((wordsList1[:index] + wordsList1[index + 1:]), wordsList2, index)
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
    if (len(wordsList1) == 0 and len(wordsList2) == 0):
        return_result_file("")
    else:
        return_result_file(mergeSort(removeDuplicates(wordsList1 + wordsList2, 0)))


def parseWords(wordsList, line, index):
    isDigit = lambda x: (x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or 
        x == '5' or x == '6' or x == '7' or x == '8' or x == '9')
    isLowerChar = lambda x: (x == 'a' or x == 'b' or x == 'c' or x == 'd' or x == 'e' or 
          x == 'f' or x == 'g' or x == 'h' or x == 'i' or x == 'j' or 
          x == 'k' or x == 'l' or x == 'm' or x == 'n' or x == 'o' or 
          x == 'p' or x == 'q' or x == 'r' or x == 's' or x == 't' or 
          x == 'u' or x == 'v' or x == 'w' or x == 'x' or x == 'y' or x == 'z')
    isUpperChar = lambda x: (x == 'A' or x == 'B' or x == 'C' or x == 'D' or x == 'E' or 
          x == 'F' or x == 'G' or x == 'H' or x == 'I' or x == 'J' or 
          x == 'K' or x == 'L' or x == 'M' or x == 'N' or x == 'O' or 
          x == 'P' or x == 'Q' or x == 'R' or x == 'S' or x == 'T' or 
          x == 'U' or x == 'V' or x == 'W' or x == 'X' or x == 'Y' or x == 'Z')
    lowerCaseIt = lambda x: chr(ord(x) + 32)

    while index < len(line):
        if isDigit(line[index]):
            if (index != 0):
                if ((isLowerChar(line[index - 1])) or (isUpperChar(line[index - 1]))):
                    wordsList.append(line[:index])
                    line = line[index:]
                    index = 0
                else:
                    index += 1
            else:
                index += 1
        elif isLowerChar(line[index]):
            if (index != 0):
                if ((isDigit(line[index - 1])) or (isDigit(line[index - 1]))):
                    wordsList.append(line[:index])
                    line = line[index:]
                    index = 0
                else:
                    index += 1
            else:
                index += 1
        elif isUpperChar(line[index]):
            lowercaseChar = lowerCaseIt(line[index])
            line = line[:index] + lowercaseChar + line[index + 1:]
            if (index != 0):
                if ((isDigit(line[index - 1])) or (isDigit(line[index - 1]))):
                    wordsList.append(line[:index])
                    line = line[index:]
                    index = 0
                else:
                    index += 1
            else:
                index += 1
        else:
            if (line[index] == "."):
                if index != 0:
                    if (index != len(line) - 1):
                        if (line[index-1] == '0' or line[index-1] == '1' or line[index-1] == '2' or line[index-1] == '3' or line[index-1] == '4' or 
                            line[index-1] == '5' or line[index-1] == '6' or line[index-1] == '7' or line[index-1] == '8' or line[index-1] == '9'):
                            if (line[index+1] == '0' or line[index+1] == '1' or line[index+1] == '2' or line[index+1] == '3' or 
                                line[index+1] == '4' or line[index+1] == '5' or line[index+1] == '6' or line[index+1] == '7' 
                                or line[index+1] == '8' or line[index+1] == '9'):
                                    index += 1
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
        if (index == 20):
            wordsList.append(line[:index])
            line = line[index:]
            index = 0

    if index != 0:
        wordsList.append(line)

    return wordsList


def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        #mid = n // 2
        #left = arr[0:mid]
        #right = arr[mid:n]
        merge_split = lambda x: (x[:len(x)//2],x[len(x)//2:]) #--------------> We set two variables within the lambda express that splits the left side and the right
        leftSide, rightSide = merge_split(arr)
        #sortedLeft = mergeSort(left)
        #sortedRight = mergeSort(right)

        
        return merged(mergeSort(leftSide),mergeSort(rightSide))
    
def merged(left,right):
    mergedArray = mergeWhileHelp([], left, right, 0, 0, len(left), len(right))
    return mergedArray

def mergeWhileHelp(list1, left, right, i,j,m,n):
    if not(i < m and j < n):
        list1.extend(left[i:])
        list1.extend(right[j:])
        return list1
    else:
        if (left[i] <= right[j]):
            list1.append(left[i])
            i += 1
        else:
            list1.append(right[j])
            j += 1
        return mergeWhileHelp(list1, left, right, i,j,m,n)


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
        if (txt_list == [] or txt_list == ""):
            result_file.write("empty set")
        else:
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
