#!/usr/bin/node

const argument = parseInt(process.argv[2]);
if (isNaN(argument)) {
    console.log('Missing size');
} else {
    let straight = 'X'
    for (let i = 0; i <= argument - 1; i++) {
        straight = straight + 'X'; 
    }
    for (let j = 0; j < argument - 1; j++) {
        console.log(straight);
    }
}
