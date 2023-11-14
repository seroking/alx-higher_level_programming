#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let l = list.length; l > 0; l--) {
    rev.push(list[l - 1]);
  }
  return rev;
};
