const fs = require('fs');

fs.readFile('a1.txt','utf-8', (err,data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});