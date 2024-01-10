#!/usr/bin/node

const arr1 = require('./100-data').list;
console.log(arr1);
console.log(arr1.map((x, idx) => x * idx));
