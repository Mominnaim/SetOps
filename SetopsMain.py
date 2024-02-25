import sys

def main():
    # Uncomment below lines if you want to get file names from command line arguments
    # fileName = sys.argv[1]
    # fileName2 = sys.argv[2]
    # listFile1 = getWords(fileName)
    # listFile2 = getWords(fileName2)

    # Or you can directly call getWords function
    listF = getWords()
    print(listF)

def getWords(txt):
    f1 = open(txt, "r")
    line = f1.read() # --------------------------------------------------------> This works 



    word = []
    parseWords(word, line, 0)                                                                 
    word = removeDuplicates(word, 0)                      
    word = mergeSort(word)

    return line

"""
    words3 = union(words, words2)
    words3 = intersection(words, words2, 0)
    #words3 = difference(words, words2, 0)
    #words3 = mergeSort(words3)
    return words3
"""

def removeDuplicates(wordsList, index):
    if index + 1 >= len(wordsList):
        return wordsList
    else:
        # Update wordsList with the result of removeDupHelp
        wordsList = removeDupHelp(wordsList, index + 1, wordsList[index])
        # Recur for the next word
        return removeDuplicates(wordsList, index + 1)
    
def intersection(wordsList1, wordsList2, index):
    if index + 1 >= len(wordsList1):
        return wordsList1
    else:
        # Update wordsList with the result of removeIntersectionHelp
        intersect = removeIntersectionHelp(wordsList2, 0, wordsList1[index])
        if (intersect):
            return intersection(wordsList1, wordsList2, index + 1)
        else:
            wordsList1 = wordsList1[:index] + wordsList1[index + 1:]
            return intersection(wordsList1, wordsList2, index)
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
        return wordsList1
    else:
        # Update wordsList with the result of removeIntersectionHelp
        different = removeDifferenceHelp(wordsList2, 0, wordsList1[index])
        if (different):
            return difference(wordsList1, wordsList2, index + 1)
        else:
            wordsList1 = wordsList1[:index] + wordsList1[index + 1:]
            return difference(wordsList1, wordsList2, index)
        # Recur for the next word
        
    
def removeDifferenceHelp(wordsList, index, target):
    if index > len(wordsList) - 1:
        return True
    elif wordsList[index] == target:
        return False
    else:
        # Recur for the next character
        return removeDifferenceHelp(wordsList, index + 1, target)
    
def union(wordsList1, wordsList2):
    wordsList = wordsList1 + wordsList2
    wordsList = removeDuplicates(wordsList, 0)
    return wordsList

def removeDupHelp(wordsList, index, target):
    if index > len(wordsList) - 1:
        return wordsList
    elif wordsList[index] == target:
        wordsList = wordsList[:index] + wordsList[index + 1:]
        # Recur for the same index as the length has reduced after removal
        return removeDupHelp(wordsList, index, target)
    else:
        # Recur for the next character
        return removeDupHelp(wordsList, index + 1, target)

def parseWords(wordsList, line, index):
    while index < len(line):
        if (line[index] in '0123456789'):
            index += 1
        elif (line[index] in 'abcdefghijklmnopqrstuvwxyz'):
            index += 1
        elif (line[index] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            lowercaseChar = chr(ord(line[index]) + 32)
            line = line[:index] + lowercaseChar + line[index + 1:]
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
    n = len(arr)
    if n <= 1:
        return arr
    else:
        mid = n // 2
        left = arr[0:mid]
        right = arr[mid:n]
        sortedLeft = mergeSort(left)
        sortedRight = mergeSort(right)
        return merged(sortedLeft,sortedRight)
    
def merged(left,right):
    mergedArray = []
    m, n = len(left), len(right)
    i, j = 0, 0
    while i < m and j < n:
        if (left[i] <= right[j]):
            mergedArray.append(left[i])
            i += 1
        else:
            mergedArray.append(right[j])
            j += 1
    mergedArray.extend(left[i:])
    mergedArray.extend(right[j:])
    return mergedArray

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Format: python setops.py \"set1=[filename]; set2=[filename];operation=[difference|union|intersection]\"")
        sys.exit(1)

    # argv[1] is the string of set1, set2, and operation and its splits it with semi colon
    args = sys.argv[1].split(';')

    # There are three elements now which each one of them being assigned a variable.
    set1 = getWords(args[0].split('=')[1])
    set2 = getWords(args[1].split('=')[1])

    print(set1)
    print(set2)

    operation = args[2].split('=')[1]


    # If the correct parameters are passed in then start the actually part of the code.
    # perform_operation(set1, set2, operation)