#!/usr/bin/node

const number = parseInt(require('process').argv[2]);

if (number) {
  for (let i = 0; i < number; i++) {
    let x = '';
    for (let j = 0; j < number; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
