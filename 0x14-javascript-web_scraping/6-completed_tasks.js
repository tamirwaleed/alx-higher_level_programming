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
    let userId = 1;
    for (let i = 0; i < results.length; i++) {
      if (results[i].completed) {
        if (finale[results[i].userId] === userId) {
          counter++;
        } else if (finale[results[i].userId] !== userId) {
          finale[userId] = counter;
          userId = results[i].userId;
          if (userId in finale) {
            finale[userId] += 1;
            counter = finale[userId];
          } else {
            finale[userId] = 1;
            counter = 1;
          }
        } else if ((results[i].userId in finale) === false) {
          finale[userId] = 1;
          counter++;
        }
      }
    }
    console.log(finale);
  }
});
