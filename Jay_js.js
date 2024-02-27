const fs = require('fs'); // Importing necessary functions from setops.js
const process = require('process');

function getWords(txt, callback) {
    let words = []
    fs.readFile(txt,'utf-8', (err,data) => {
        if (err) {
            console.error(err);
            callback(err, null);
        } else{
            callback(null,mergeSort(removeDuplicates(parseWords(words, data, 0), 0)));
        }
    });
        
}


function removeDuplicates(wordsList, index) {
    if (index + 1 > wordsList.length) {
        return wordsList;
    } else {
        return removeDuplicates(removeDupHelp(wordsList, index + 1, wordsList[index]), index + 1);
    }
}

function removeDupHelp(wordsList, index, target) {
    if (index > wordsList.length - 1) {
        return wordsList;
    } else if (wordsList[index] === target) {
        return removeDupHelp(wordsList.slice(0, index).concat(wordsList.slice(index + 1)), index, target);
    } else {
        return removeDupHelp(wordsList, index + 1, target);
    }
}

function intersection(wordsList1, wordsList2, index) {
    if (index > wordsList1.length - 1) {
        return_result_file(wordsList1);
    } else {
        if (removeIntersectionHelp(wordsList2, 0, wordsList1[index])) {
            return intersection(wordsList1, wordsList2, index + 1);
        } else {
            return intersection(wordsList1.slice(0, index).concat(wordsList1.slice(index + 1)), wordsList2, index);
        }
    }
}

function removeIntersectionHelp(wordsList, index, target) {
    if (index > wordsList.length - 1) {
        return false;
    } else if (wordsList[index] === target) {
        return true;
    } else {
        return removeIntersectionHelp(wordsList, index + 1, target);
    }
}

function difference(wordsList1, wordsList2, index) {
    if (index >= wordsList1.length) {
        return_result_file(wordsList1);
    } else {
        if (removeDifferenceHelp(wordsList2, 0, wordsList1[index])) {
            return difference(wordsList1, wordsList2, index + 1);
        } else {
            return difference(wordsList1.slice(0, index).concat(wordsList1.slice(index + 1)), wordsList2, index);
        }
    }
}

function removeDifferenceHelp(wordsList, index, target) {
    if (index > wordsList.length - 1) {
        return true;
    } else if (wordsList[index] === target) {
        return false;
    } else {
        return removeDifferenceHelp(wordsList, index + 1, target);
    }
}

function union(wordsList1, wordsList2) {
    return_result_file(mergeSort(removeDuplicates(wordsList1.concat(wordsList2), 0)));
}


function parseWords(wordsList, line, index) {
    const isDigit = (x) => ('0123456789'.indexOf(x) !== -1);
    const isLowerChar = (x) => ('abcdefghijklmnopqrstuvwxyz'.indexOf(x.toLowerCase()) !== -1);
    const isUpperChar = (x) => ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.indexOf(x) !== -1);
    const lowerCaseIt = (x) => String.fromCharCode(x.charCodeAt(0) + 32);

    while (index < line.length) {
        if (isDigit(line[index])) {
            if (index !== 0) {
                if (isLowerChar(line[index - 1]) || isUpperChar(line[index - 1])) {
                    wordsList.push(line.slice(0, index));
                    line = line.slice(index);
                    index = 0;
                } else {
                    index++;
                }
            } else {
                index++;
            }
        } else if (isUpperChar(line[index])) {
            const lowercaseChar = lowerCaseIt(line[index]);
            line = line.slice(0, index) + lowercaseChar + line.slice(index + 1);
            if (index !== 0) {
                if (isDigit(line[index - 1]) || isDigit(line[index - 1])) {
                    wordsList.push(line.slice(0, index));
                    line = line.slice(index);
                    index = 0;
                } else {
                    index++;
                }
            } else {
                index++;
            }
        }
        else if (isLowerChar(line[index])) {
            if (index !== 0) {
                if (isDigit(line[index - 1]) || isDigit(line[index - 1])) {
                    wordsList.push(line.slice(0, index));
                    line = line.slice(index);
                    index = 0;
                } else {
                    index++;
                }
            } else {
                index++;
            }
        }  else {
            if (line[index] === ".") {
                if (index !== 0) {
                    if (index !== line.length - 1) {
                        if ('0123456789'.indexOf(line[index - 1]) !== -1) {
                            if ('0123456789'.indexOf(line[index + 1]) !== -1) {
                                index++;
                            } else {
                                wordsList.push(line.slice(0, index));
                                line = line.slice(index + 1);
                                index = 0;
                            }
                        } else {
                            wordsList.push(line.slice(0, index));
                            line = line.slice(index + 1);
                            index = 0;
                        }
                    } else {
                        wordsList.push(line.slice(0, index));
                        line = line.slice(index + 1);
                        index = 0;
                    }
                } else {
                    line = line.slice(index + 1);
                    index = 0;
                }
            } else {
                if (index !== 0) {
                    wordsList.push(line.slice(0, index));
                }
                line = line.slice(index + 1);
                index = 0;
            }
        }
        if (index === 20) {
            wordsList.push(line.slice(0, index));
            line = line.slice(index);
            index = 0;
        }
    }

    if (index !== 0) {
        wordsList.push(line);
    }
    return wordsList;
}


function mergeSort(arr) {
    const n = arr.length;
    if (n <= 1) {
        return arr;
    } else {
        const mid = Math.floor(n / 2);
        const left = arr.slice(0, mid);
        const right = arr.slice(mid);
        const sortedLeft = mergeSort(left);
        const sortedRight = mergeSort(right);
        return merged(sortedLeft, sortedRight);
    }
}

function merged(left, right) {
    const mergedArray = [];
    let i = 0, j = 0;
    const m = left.length, n = right.length;
    return mergeWhileHelp(mergedArray, left, right, i, j, m, n);
}

function mergeWhileHelp(list1, left, right, i, j, m, n) {
    if (!(i < m && j < n)) {
        list1.push(...left.slice(i));
        list1.push(...right.slice(j));
        return list1;
    } else {
        if (left[i] <= right[j]) {
            list1.push(left[i]);
            i++;
        } else {
            list1.push(right[j]);
            j++;
        }
        return mergeWhileHelp(list1, left, right, i, j, m, n);
    }
}

function perform_operation(txt1, txt2, operation) {
    getWords(txt1, (err, words1) => {
        if (err) {
            console.error(`Error reading file ${txt1}: ${err.message}`);
            process.exit(1);
        }

        getWords(txt2, (err, words2) => {
            if (err) {
                console.error(`Error reading file ${txt2}: ${err.message}`);
                process.exit(1);
            }

            if (operation === 'difference') {
                difference((words1),(words2), 0);
            } else if (operation === 'union') {
                union((words1),(words2));
            } else if (operation === 'intersection') {
                intersection((words1), (words2), 0);
            } else {
                console.log("Sorry, but that is not a valid operation.");
                process.exit(1);
            }

        });
    });
}


function return_result_file(txtList) {
    fs.writeFileSync('result.txt', txtList.length === 0 || txtList === "" ? "empty set" : txtList.join('\n'));
}



if (require.main === module) {
    if (require.main === module) {
        try {
            if (process.argv.length !== 3) {
                console.log("Format: node setops.js \"set1=[filename]; set2=[filename];operation=[difference|union|intersection]\"");
                process.exit(1);
            }
    
            const args = process.argv[2].split(';');
    
            perform_operation(args[0].split('=')[1], args[1].split('=')[1], args[2].split('=')[1]);
    
        } catch (error) {
            console.log("Error in formatting. Format: node setops.js \"set1=[filename]; set2=[filename];operation=[difference|union|intersection]\"");
        }
    }
}