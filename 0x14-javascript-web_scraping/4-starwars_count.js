#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let counter = 0;
request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const results = JSON.parse(body)['results'];
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i]['characters'].length; j++) {       
        if (results[i]['characters'][j].endsWith('18/')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
