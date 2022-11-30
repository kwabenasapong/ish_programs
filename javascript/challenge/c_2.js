#!/usr/bin/node
const converter = require('./10-converter').converter;

function checkArg (x, base) {
  const number = parseInt(x, base);
  if (isNaN(number)) { return 0; }
  return number;
}

if (process.argv.length <= 2 || checkArg(process.argv[2], 10) === 0) {
  console.log('Missing number of occurrences');
  process.exit(1);
} else {
  const x = process.argv.length;
  const len = parseInt(x) - 2;
  //console.log(len);
  //console.log(parseInt(process.argv[2]));
  let i = 2;
  let myConverter_10 = converter(10);
  let myConverter_16 = converter(6);
  while (i < len) {
    let number = myConverter_10(parseInt(process.argv[i], 2));
    if (i === 2) {console.log(typeof(number));}
    if (i % 11 === 0) {
      console.log();
    }
    process.stdout.write(number);
    //process.stdout.write(String.fromCharCode(parseInt(number)));
    i++;
  }
}
