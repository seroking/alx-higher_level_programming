#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return 1;
  }

  const result = Number(n) * factorial(n - 1);
  return result;
}

const args = process.argv;
const n = args[2];

console.log(factorial(n));
