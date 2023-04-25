#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/';
const id = parseInt(process.argv[2], 10);

request(url, function (err, response, body) {
  if (!err) {
    try {
      const resp = JSON.parse(body);
      const results = resp.results;
      const targetId = id < 4 ? id + 3 : id - 3;
      const targetFilm = results.find(
        result => result.episode_id === targetId);
      const characters = targetFilm.characters;
      characters.forEach(url => {
        request(url, function (err, response, body) {
          if (!err) {
            try {
              console.log(JSON.parse(body).name);
            } catch (error) {
              console.error(
                'Error parsing character JSON:', error);
            }
          } else {
            console.error(
              'Error requesting character:', err);
          }
        });
      });
    } catch (error) {
      console.error('Error parsing film JSON:', error);
    }
  } else {
    console.error('Error requesting film:', err);
  }
});
