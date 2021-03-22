#!/usr/bin/node

const number = parseInt(process.argv[2]);
if (number === undefined || isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}

function factorial (x) {
  if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
