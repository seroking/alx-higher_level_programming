#!/usr/bin/node
const args = process.argv;
let count = 0;
while (args[count] !== undefined) {
  count++;
}
console.log(count === 2 ? 'No argument' : args[2]);
