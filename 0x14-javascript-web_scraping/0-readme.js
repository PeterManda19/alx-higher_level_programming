#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: node script.js filename');
  process.exit(1);
}

fs.readFile(process.argv[2], 'utf8', function (
    error, content) {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log(content);
});
