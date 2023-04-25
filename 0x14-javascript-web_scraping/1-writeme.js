#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 4) {
  console.error(
    'Usage: node script.js filename content');
  process.exit(1);
}

fs.writeFile(
    process.argv[2], process.argv[3], error => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log('File written successfully');
});
