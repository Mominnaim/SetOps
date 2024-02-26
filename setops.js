const fs = require('fs');

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
    if (index >= wordsList1.length - 1) {
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
    
    while (index < line.length) {
        if (/[0123456789]/.test(line[index])) {
            index += 1;
        } else if (/[a-z]/.test(line[index])) {
            index += 1;
        } else if (/[A-Z]/.test(line[index])) {
            line =
                line.slice(0, index) +
                String.fromCharCode(line.charCodeAt(index) + 32) +
                line.slice(index + 1);
            index += 1;
        } else {
            if (line[index] === ".") {
                if (index !== 0) {
                    if (index !== line.length - 1) {
                        if (/[0123456789]/.test(line[index - 1])) {
                            if (/[012345679]/.test(line[index + 1])) {
                                index += 1;
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
    }

    if (index !== 0) {
        wordsList.push(line);
    }

    return wordsList
}

function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    } else {
        return merged(mergeSort(arr.slice(0, Math.floor(arr.length / 2))), mergeSort(arr.slice(Math.floor(arr.length / 2))), 0, 0);
    }
}


function merged(left, right, i, j) {
    let mergedArray = [];
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            mergedArray.push(left[i]);
            i++;
        } else {
            mergedArray.push(right[j]);
            j++;
        }
    }
    mergedArray.push(...left.slice(i), ...right.slice(j));
    return mergedArray;
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
    fs.writeFileSync('result.txt', txtList.join('\n'), 'utf-8');
}


if (require.main === module) {
    if (process.argv.length !== 3) {
        console.log("Format: node setops.js \"set1=[filename]; set2=[filename];operation=[difference|union|intersection]\"");
        process.exit(1);
    }

    const args = process.argv[2].split(';');


    perform_operation((args[0].split('=')[1]), (args[1].split('=')[1]), args[2].split('=')[1]);
}
