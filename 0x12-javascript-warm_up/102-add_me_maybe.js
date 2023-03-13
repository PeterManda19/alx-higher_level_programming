#!/usr/bin/node
export function addMeMaybe (number, theFunction) {
    return theFunction(++number);
}