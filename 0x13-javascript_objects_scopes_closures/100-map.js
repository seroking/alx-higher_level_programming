#!/usr/bin/node

const arr1 = require('./100-data').list;

const arr2 = arr1.map((x, idx) => x * idx);

console.log(arr1);
console.log(arr2);
