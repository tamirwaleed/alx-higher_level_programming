#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function printInOrder (chars, i) {
  request(chars[i], (error, response, body) => {
    if (error) {
      console.log('error:', error);
    } else {
      console.log(JSON.parse(body).name);
      if (i + 1 < chars.length) {
        printInOrder(chars, i + 1);
      }
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const chars = JSON.parse(body).characters;
    printInOrder(chars, 0);
  }
});
