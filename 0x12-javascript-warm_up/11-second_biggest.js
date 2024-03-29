#!/usr/bin/node

const args = process.argv;
const len = args.length;
const intArr = []; let i = 2; let intMax = 0; let secMax = 0;

if (len < 4) {
  console.log(0);
} else {
  while (args[i]) {
    intArr.push(parseInt(args[i]));
    i++;
  }
  intMax = Math.max(...intArr);
  intArr.splice(intArr.indexOf(intMax), 1);
  secMax = Math.max(...intArr);
  console.log(secMax);
}
