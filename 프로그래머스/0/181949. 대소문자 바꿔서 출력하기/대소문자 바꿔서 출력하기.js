const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let result = '';

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    // const length = str.length;
    for (const char of str){
        if ( char === char.toUpperCase() ){
            result += char.toLowerCase()
        }
        else {
            result += char.toUpperCase()
        }
    }
    
    console.log(result);
});