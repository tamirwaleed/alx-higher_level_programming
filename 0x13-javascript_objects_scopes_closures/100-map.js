#!/usr/bin/node
const myArray = require('./100-data').list;
const newList = myArray.map((x) => myArray.indexOf(x) * parseInt(x));
console.log(myArray);
console.log(newList);
