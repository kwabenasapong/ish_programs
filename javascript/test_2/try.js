#!/usr/bin/node
const x = function (a, func) {
  for (let i = 0; i < a; i++)
  {
    func();
  };
}
x(3, function () { 
  console.log('who are you');
});
