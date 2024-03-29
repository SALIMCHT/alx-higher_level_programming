#!/usr/bin/node

const N = parseInt(process.argv[2]);

if (isNaN(N) || N === 0) {
  console.log(1);
} else {
  function getFact (n) {
    if (n >= 1) {
      return n * getFact(n - 1);
    } else {
      return 1;
    }
  }

  console.log(getFact(N));
}
