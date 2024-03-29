#!/usr/bin/node

const argv = require('process').argv;
const number = parseInt(argv[2]);

if (number) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
