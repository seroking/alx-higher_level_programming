#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      occ++;
    }
  }
  return occ;
};
