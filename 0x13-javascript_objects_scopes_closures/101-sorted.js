#!/usr/bin/node

const cursedDict = require('./101-data').dict;

const damenDict = {};

for (const UId in cursedDict) {
  const occNum = cursedDict[UId];
  // console.log(`UID: ${UId}, occNum:${occNum}`);

  if (damenDict[occNum] === undefined) {
    damenDict[occNum] = [UId];
  } else {
    damenDict[occNum].push(UId);
  }
}
console.log(damenDict);
