#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const chars = JSON.parse(body).characters;
    for (let i = 0; i < chars.length; i++) {
      request(chars[i], (error, response, body) => {
        if (error) {
          console.log('error:', error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
