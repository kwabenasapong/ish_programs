#!/usr/bin/node
//THE SIMPLEST MODULE
require('./hello.js');

//PATTERN 1: DEFINE A GLOBAL
require('./foo.js');
foo();

//PATTERN 2: EXPORT AN ANONYMOUS FUNCTION
var bar = require('./bar.js');
bar();

//PATTERN 3: EXPORT A NAMED FUNCTION
var fiz = require('./fiz.js').fiz;
fiz();

//PATTERN 4: EXPORT AN ANONYMOUS OBJECT
var buz = require('./buz.js')
buz.log();

//PATTERN 5: EXPORT A NAMED OBJECT
var baz = require('./baz.js').Baz;
baz.log();

//PATTERN 6: EXPORT AN ANONYMOUS PROTOTYPE
var Doo = require('./doo.js');
var doo = new Doo();
doo.log();

//PATTERN 7: EXPORT A NAMED PROTOTYPE
var Qux = require('./qux.js').Qux;
var qux = new Qux();
qux.log();
