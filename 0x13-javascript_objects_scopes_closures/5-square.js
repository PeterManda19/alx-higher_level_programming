#!/usr/bin/node
export default class Square extends require('./4-rectangle') {
    constructor (size) {
      super(size, size);
    }
}
