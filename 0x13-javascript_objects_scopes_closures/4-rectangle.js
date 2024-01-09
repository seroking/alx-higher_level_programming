#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let figure = '';
    for (let i = 0; i < this.width; i++) {
      figure = figure + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(figure);
    }
  }

  rotate () {
    const a = this.height;
    this.height = this.width;
    this.width = a;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
};
