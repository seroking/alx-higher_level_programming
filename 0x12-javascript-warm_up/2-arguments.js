#!/usr/bin/node
const args = process.argv.length - 2;
console.log(args === 0 ? 'No argument' : args === 1 ? 'Argument found' : 'Arguments found');
