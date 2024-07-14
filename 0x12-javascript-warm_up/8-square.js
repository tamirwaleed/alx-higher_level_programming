#!/usr/bin/node
let myRow = '';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    myRow += 'X';
  }
  for (let j = 0; j < parseInt(process.argv[2]); j++) {
    console.log(myRow);
  }
}
