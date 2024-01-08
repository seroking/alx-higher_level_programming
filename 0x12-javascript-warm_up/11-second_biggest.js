#!/usr/bin/node
function sec (numbers) {
  const nums = [];
  if (numbers.length <= 3) {
    return (0);
  }
  for (let i = 2; i <= numbers.length - 1; i++) {
    nums[i - 2] = parseInt(numbers[i]);
  }
  nums.sort(function (a, b) {
    return a - b;
  });
  return (nums[nums.length - 2]);
}
  console.log(sec(process.argv));