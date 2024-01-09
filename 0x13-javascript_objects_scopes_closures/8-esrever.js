#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  const li = list;
  const l = list.length;
  for (let i = 0; i < l; i++) {
    rev.push(li.pop());
  }
  return (rev);
};
