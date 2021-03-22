#!/usr/bin/node

const argLength = process.argv.length;
if (argLength < 4) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  const second = list.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
