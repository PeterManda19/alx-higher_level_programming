#!/usr/bin/node
import { readFileSync, writeFileSync } from 'fs';
const src1 = readFileSync(process.argv[2], 'utf8');
const src2 = readFileSync(process.argv[3], 'utf8');
writeFileSync(process.argv[4], src1 + src2);
