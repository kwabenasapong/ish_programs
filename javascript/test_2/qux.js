#!/usr/bin/node
var Qux = function () {};

Qux.prototype.log = function () {
  console.log('qux!');
}

exports.Qux = Qux;
