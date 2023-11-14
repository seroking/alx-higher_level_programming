#!/usr/bin/node
function findSecondLargest(args) {
  if (args.length <= 2) {
    console.log(0);
    return;
  }
  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 2; i < args.length; i++) {
    const currentNumber = Number(args[i]);
    if (currentNumber > largest) {
      secondLargest = largest;
      largest = currentNumber;
    } else if (currentNumber > secondLargest && currentNumber < largest) {
      secondLargest = currentNumber;
    }
  }
  console.log(secondLargest !== -Infinity ? secondLargest : 0);
}
let args = process.argv;
findSecondLargest(args);





