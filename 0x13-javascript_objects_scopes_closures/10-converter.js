#!/usr/bin/node
export function converter (base) {
    return function (dec) {
      return dec.toString(base);
    };
}
