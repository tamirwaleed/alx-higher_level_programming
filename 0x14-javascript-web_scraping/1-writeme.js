#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];
try {
  fs.writeFileSync(filepath, content, 'utf8');
} catch (err) {
  console.error(err);
}
