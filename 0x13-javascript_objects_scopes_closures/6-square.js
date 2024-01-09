#!/usr/bin/node
const Squareim = require('./5-square');

class Square extends Squareim {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      let figure = '';
      for (let i = 0; i < this.height; i++) {
        figure = figure + 'X';
      }
      for (let i = 0; i < this.height; i++) {
        console.log(figure);
      }
    } else {
      let figure = '';
      for (let i = 0; i < this.height; i++) {
        figure = figure + c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(figure);
      }
    }
  }
}

module.exports = Square;
