#!/usr/bin/node
args = process.argv;
let is_converted = Number.isInteger(Number(args[2]));
console.log(is_converted === true ? 'My number: ' + Number(args[2]) : 'Not a number');
