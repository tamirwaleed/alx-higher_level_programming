#!/usr/bin/node
const myArray = require('./100-data').list;
let i = 0;
const newList = myArray.map((x) => {
	return (i++ * parseInt(x));
});
console.log(myArray);
console.log(newList);
