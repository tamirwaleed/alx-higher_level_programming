#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const finale = {};
request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const results = JSON.parse(body);
    const userId = 10;
    for (let i = 0; i < results.length; i++) {
      if (results[i].completed) {
        if (finale[results[i].userId]) {
          finale[results[i].userId]++;
        } else {
          finale[results[i].userId] = 1;
        }
      }
    }
  }
  console.log(finale);
});
