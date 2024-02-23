const fs = require('fs')

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

function setIntersection(txt1, txt2){

    list1 = new Set(fileIntoAList(txt1));
    list2 = new Set(fileIntoAList(txt2));

    const intersectionResult = Array.from(set1).filter(item => set2.has(item)).sort();

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