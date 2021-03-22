#!/usr/bin/node

const argument = process.argv[2];
if (isNaN(argument)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i <= argument - 1; i++) {
        console.log('C is fun'); 
    }
}
