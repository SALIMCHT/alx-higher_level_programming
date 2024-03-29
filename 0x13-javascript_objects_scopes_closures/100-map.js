#!/usr/bin/node
const cursedList = require('./100-data').list;

const damenList = cursedList.map(function (num, indx) {
  return num * indx;
});

/*
for (let i = 0; i < cursedList.length; i++) {
  damenList[i] = cursedList[i] * i;
}
*/
console.log(cursedList);
console.log(damenList);
