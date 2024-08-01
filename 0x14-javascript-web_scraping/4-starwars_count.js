#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let counter = 0;
const wedge = 'http://swapi-api.alx-tools.com/api/people/18/';
request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.includes(wedge)) {
        counter++;
      }
    }
    console.log(counter);
  }
});
