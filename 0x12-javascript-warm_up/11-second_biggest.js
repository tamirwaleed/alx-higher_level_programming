#!/usr/bin/node
function secondBig () {
  if (process.argv.length < 4) {
    return 0;
  } else {
    let i = parseInt(process.argv[2]);
    let a;
    let b = parseInt(process.argv[3]);
    for (let j = 2; j < process.argv.length; j++) {
      a = parseInt(process.argv[j]);
      if (a > i) {
        b = i;
        i = a;
      } else if (a < i && a > b) {
        b = a;
      }
    }
    return b;
  }
}
console.log(secondBig());
