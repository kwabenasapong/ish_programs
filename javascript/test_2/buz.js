#!/usr/bin/node
var Buz = function () {};

Buz.prototype.log = function () {
  console.log('buz!');
};

module.exports = new Buz();
