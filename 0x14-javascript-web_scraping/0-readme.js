#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
try {
	const theData = fs.readFileSync(filepath, 'utf8');
	console.log(theData);
} catch (err) {
	console.log(err);
};
