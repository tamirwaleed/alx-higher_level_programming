#!/usr/bin/node
const myDict = require('./101-data').dict;
const newDict = {};
for (const N in myDict) {
	    if (newDict[myDict[N]] === undefined) {
		    	newDict[myDict[N]] = [];
		        }
	    newDict[myDict[N]].push(N);
}
console.log(newDict);
