#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filepath = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const content = console.log(JSON.parse(body));
  }
});
try {
  fs.writeFileSync(filepath, content, 'utf8');
} catch (err) {
  console.error(err);
};
