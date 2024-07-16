#!/usr/bin/node
exports.converter = function (base) {
  return function (theNum) {
    return theNum.toString(base);
  };
};
