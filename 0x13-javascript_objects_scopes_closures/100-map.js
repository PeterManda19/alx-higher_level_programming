#!/usr/bin/node
import { list } from './100-data.js';
console.log(list);
console.log(list.map((x, xI) => x * xI));
