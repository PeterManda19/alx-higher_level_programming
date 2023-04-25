#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const BaseUrl = 'https://swapi-api.hbtn.io/api';
request(
    BaseUrl + '/films/' + argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const data = JSON.parse(body);
      console.log(data.title);
    } catch (error) {
      console.error(`Error parsing JSON: ${error}`);
    }
  }
});
