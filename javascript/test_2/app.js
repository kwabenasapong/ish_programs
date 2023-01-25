#!/usr/bin/node
// THE SIMPLEST MODULE
require('./hello.js');

// PATTERN 1: DEFINE A GLOBAL
require('./foo.js');
foo();

// PATTERN 2: EXPORT AN ANONYMOUS FUNCTION
const bar = require('./bar.js');
bar();

// PATTERN 3: EXPORT A NAMED FUNCTION
const fiz = require('./fiz.js').fiz;
fiz();

// PATTERN 4: EXPORT AN ANONYMOUS OBJECT
const buz = require('./buz.js');
buz.log();

// PATTERN 5: EXPORT A NAMED OBJECT
const baz = require('./baz.js').Baz;
baz.log();

// PATTERN 6: EXPORT AN ANONYMOUS PROTOTYPE
const Doo = require('./doo.js');
const doo = new Doo();
doo.log();

// PATTERN 7: EXPORT A NAMED PROTOTYPE
const Qux = require('./qux.js').Qux;
const qux = new Qux();
qux.log();
