#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let counter = 0;
const finale = {};
request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const results = JSON.parse(body);
    let userId = results[0].userId;
    for (let i = 0; i < results.length; i++) {
      if (results[i].completed) {
        if (finale[results[i].userId] === userId) {
          counter++;
        } else if (finale[results[i].userId] !== userId) {
          finale[userId] = counter;
          userId = finale[results[i].userId];
          finale[userId] += 1;
          counter = 0;
        } else {
          finale[userId] = 1;
          counter++;
        }
      }
    }
    console.log(finale);
  }
});
