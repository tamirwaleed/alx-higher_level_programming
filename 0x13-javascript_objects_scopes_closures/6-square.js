#!/usr/bin/node
const squareParent = require('./5-square');

module.exports = class Square extends squareParent {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(row);
      }
    }
  }
};
