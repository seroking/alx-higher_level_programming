#!/usr/bin/node

const arr1 = require('./100-data');

const arr2 = arr1.list.map((x, idx) => x * idx);

console.log(arr1.list);
console.log(arr2);
