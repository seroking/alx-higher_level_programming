#!/usr/bin/node
const args = process.argv;
const x = args[2];
const isConverted = Number.isInteger(Number(args[2]));

if (isConverted) {
  for (let i = 1; i <= x; i++) {
    console.log('X'.repeat(x));
  }
} else {
  console.log('Missing size');
}
