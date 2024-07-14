#!/usr/bin/node
function secondBig () {
  if (process.argv.length < 3) {
    console.log(0);
  } else {
    let i = process.argv[2];
    let a;
    let b = process.argv[2];
    for (let j = 2; j < process.argv.length; j++) {
      a = process.argv[j];
      if (a > i) {
        i = process.argv[j];
      } else if (a < i && a > b) {
        b = process.argv[j];
      }
    }
    return b;
  }
}
console.log(secondBig());
