#!/usr/bin/node
exports.logMe = (function (item) {
  let itemCount = -1;
  return function (item) {
    itemCount += 1;
    console.log(itemCount + ': ' + item);
  };
})();
