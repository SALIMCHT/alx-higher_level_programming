#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isFinite(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let Rbuff = '';
      for (let i = 0; i < this.width; i++) { Rbuff += 'X'; }
      console.log(Rbuff);
    }
  }
}

module.exports = Rectangle;
