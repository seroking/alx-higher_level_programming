#!/usr/bin/node
const args = process.argv;
const isConverted = Number.isInteger(Number(args[2]));
console.log(isConverted === true ? 'My number: ' + Number(args[2]) : 'Not a number');
