#!/usr/bin/node
let count = 0;
export function logMe (item) {
  console.log(`${count++}: ${item}`);
}
