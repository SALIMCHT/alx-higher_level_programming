#!/usr/bin/node

const PSquare = require('./5-square');

class Square extends PSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let Rbuff = '';
      for (let i = 0; i < this.width; i++) { Rbuff += c; }
      console.log(Rbuff);
    }
  }
}
module.exports = Square;
