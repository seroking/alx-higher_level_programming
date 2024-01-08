#!/usr/bin/node
if (isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    let square = '';
    for (let i = 0; i < process.argv[2]; i++) {
      square = 'X' + square;
    }
    for (let i = 0; i < process.argv[2]; i++) {
      console.log(square);
    }
  }