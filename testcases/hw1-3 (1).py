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

def getWords():
    # Uncomment below lines if you want to read from a file
    # f1 = open(fileNameStr, "r")
    # line = f1.readline()
    line = "tree, 12.34 Blue. 5678\nhot. 91011 rock 12.13\nstar 91011 Moon. 91.012"
    line2 = "cold, 12.34 blue 5678\ntree. 91011 rock 12.13\nstar, 91011 moon. 91.011 fast2go hi"
    words = []
    parseWords(words, line2, 0)
    words = removeDuplicates(words, 0)
    words = mergeSort(words)
    #words2 = []
    #parseWords(words2, line, 0)
    #words2 = removeDuplicates(words2, 0)
    #words2 = mergeSort(words2)
    #words3 = union(words, words2)
    #words3 = intersection(words, words2, 0)
    #words3 = difference(words, words2, 0)
    #words3 = mergeSort(words3)
    return words

def removeDuplicates(wordsList, index):
    if index + 1 >= len(wordsList):
        return wordsList
    else:
        # Update wordsList with the result of removeDupHelp
        wordsList = removeDupHelp(wordsList, index + 1, wordsList[index])
        # Recur for the next word
        return removeDuplicates(wordsList, index + 1)
    
def intersection(wordsList1, wordsList2, index):
    if index >= len(wordsList1):
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
            lowercaseChar = chr(ord(line[index]) + 32)
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
    if index != 0:
        wordsList.append(line)


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
    mergedArray = mergeWhileHelp(mergedArray, left, right, i,j,m,n)
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
main()
