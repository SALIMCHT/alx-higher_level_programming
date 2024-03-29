#!/usr/bin/node

const num = require('process').argv[2];

const factorial = n => {
  if (!n) {
    return 1;
  }
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

console.log(factorial(parseInt(num)));
