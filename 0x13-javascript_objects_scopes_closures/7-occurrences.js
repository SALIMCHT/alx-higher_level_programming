#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let j = 0;
  if (list.length < 1 || !list) { return null; }
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { j++; }
  }
  return j;
};
