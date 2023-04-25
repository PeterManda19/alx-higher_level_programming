#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filepath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(`Error requesting ${url}: ${error}`);
  } else if (response.statusCode !== 200) {
    console.error(
        `Request to ${url} returned status code ${response.statusCode}`);
  } else {
    const fileStream = fs.createWriteStream(filepath);
    fileStream.on('error', function (error) {
      console.error(`Error writing to file ${filepath}: ${error}`);
    });
    fileStream.on('finish', function () {
      console.log(`File ${filepath} saved successfully`);
    });
    request(url).pipe(fileStream);
  }
});
