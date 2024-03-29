#!/usr/bin/node

function callMeMayBe (x, theFunction) {
  for (let i = 0; i < x; i++) { theFunction(); }
}
module.exports =
{
  callMeMoby: callMeMayBe
};
