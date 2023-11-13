#!/usr/bin/node
function add (a, b) {
  console.log(Number(a) + Number(b));
}
const args = process.argv;
const a = args[2];
const b = args[3];

add(a, b);
