const fs = require('fs');
const { default: test } = require('node:test');

function readfile(filename) {
    try {
        const fileContent = fs.readFile(filename, 'utf-8');
        return fileContent;
    } catch (error){
        console.error('Error in reading the file ${filename}: ${error.message}')
        process.exit(1);
    }
}

function setOperation(txt1, txt2, operation) {
    if (operation === 'intersection') {
        setIntersection(txt1, txt2);

    } else if (operation === 'union'){
        setUnion(txt1, txt2);

    } else if (operation === 'difference') {
        setDifference(txt1,txt2);

    }else {
        console.log("Sorry that is not a valid operator");
        process.exit(1);
    }
}

function setIntersection(txt1, txt2){

    list1 = new Set(fileIntoAList(txt1));
    list2 = new Set(fileIntoAList(txt2));

    const intersectionResult = Array.from(list1).filter(item => list2.has(item)).sort();

    const resultFile = 'result.txt';

    const resultString = intersectionResult.join('\n');
    fs.writeFileSync(resultFile, resultString, 'utf-8');

}

function setUnion(txt1, txt2) {
    const set1 = new Set(fileIntoAList(txt1));
    const set2 = new Set(fileIntoAList(txt2));

    const unionResult = Array.from(new Set([set1,set2])).sort();

    const resultFile = 'result.txt';
    fs.writeFileSync(resultFile, unionResult.join('\n'),'utf-8')

}

function setDifference(txt1, txt2){

    const set1 = new Set(fileIntoAList(txt1));
    const set2 = new Set(fileIntoAList(txt2));

    const differeceResult = Array.from(set1).filter(item => !set2.has(item)).sort();

    const resultFile = 'result.txt';
    fs.writeFileSync(resultFile, differeceResult.join('\n'), 'utf-8')

}

function fileIntoAList(txt) {

    const skip = /[!@#$%^?&<>`~;:]/;
    const separator1 = /[. +\-=/*()\n' ]/;
    const numbers = /[0-9]/;

    // Create empty arrays
    const funnelList = [];
    const mainList = [];

    try {
        const fileContent = fs.readfile(txt,'utf-8');

        // Itterate through every character in the string.
        for (let x = 0; x < fileContent.length -1; x++) {

            // Checks to see of the current index is skip symbols
            if (skip.test(fileContent[x])){
                continue
            }

            // Checks to see if the current index is an seperator
            else if (separator1.test(fileContent[x])) {

                // Checks to see if it a .
                if (fileContent[x] === "." && x !== 0){

                    // Checks to see if the index behind is a number and the index infront is a letter or vice versa, or If they are both letters
                    if ((numbers.test(fileContent[x+1]) && !numbers.test(fileContent[x-1])) || (!numbers.test(fileContent[x+1]) && numbers.test(fileContent[x-1])) || (!numbers.test(fileContent[x+1]) && !numbers.test(fileContent[x-1]))) {

                        // If there is nothing in the funnel list, then just continue, but if there is sometthing than push that and empty the list.
                        if (funnelList.length === 0){
                            continue
                        } else {
                            const newWord = funnelList.join('');
                            mainList.push(newWord)
                            funnelList.length = 0;
                        }

                    // If both the indexes behind and after the period is a number we will append the period.
                    } else if (numbers.test(fileContent[x+1]) && numbers.test(fileContent[x-1])) {

                        funnelList.push(fileContent[x])
                    }
                
                // If the index is not a . then come here
                } else {

                    if (funnelList.length !== 0) {
                        const newWord = funnelList.join('');
                        mainList.push(newWord)
                        funnelList.length = 0;
                        
                    } else {
                        continue
                    }
                } 

            } else {

                if ((!numbers.test(fileContent[x]) && numbers.test(fileContent[x-1])) || ((numbers.test(fileContent[x]) && !numbers.test(fileContent[x-1]) && !separator1.test)) || (x === fileContent.length - 1)) {

                    funnelList.push(fileContent[x])
                    const newWord = funnelList.join('');
                    mainList.push(newWord)
                    funnelList.length = 0;

                } else {
                    funnelList.push(fileContent[x])
                }

            }

        } 
        
        // Assuming mainList is an array containing strings and other types
        const lowercasedList = mainList.map(item => typeof item === 'string' ? item.toLowerCase() : item);

        // Return lowercasedList
        return lowercasedList;
    } catch (error) {
        if(error.code === 'enoent') {
            throw error
        }
    }

} 



if (require.main === module) {
    if (process.argv.length !== 3) {
        console.log("Format: node setops.js \"set1=[filename]; set2=[filename];operation=[difference|union|intersection]\"");
        process.exit(1);
    }

    const args = process.argv[2].split(';');

    const set1 = readfile(args[0].split('=')[1]);
    const set2 = readfile(args[1].split('=')[1]);
    const operation = args[2].split('=')[1];

    setOperation(set1, set2, operation)

}