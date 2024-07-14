#!/usr/bin/node
function factorial (n = parseInt(process.argv[2])) {
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
      return n * factorial(n - 1);
  }
}

console.log(factorial());
