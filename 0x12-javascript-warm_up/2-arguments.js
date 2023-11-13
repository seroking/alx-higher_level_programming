#!/usr/bin/node

const args_l = process.argv.length - 2;

console.log(args_l === 0 'No argument' : args_l === 1 'Argument found' : 'Arguments found')
