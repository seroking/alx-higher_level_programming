#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (!list) {
    return (0);
  }
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count = count + 1;
    }
  }
  return (count);
};
