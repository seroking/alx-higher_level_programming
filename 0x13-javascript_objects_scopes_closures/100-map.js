#!/usr/bin/node

const imp = require('./100-data');
const arr1 = imp.list;
const arr2 = arr1.map((x, idx) => x * idx);

console.log(arr1);
console.log(arr2);
