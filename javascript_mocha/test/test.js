var assert = require('assert');
var target = require('../target');

describe('Calc', function () {
  describe('#add()', function () {
    it('should add 1 and 2', function () {
      assert.equal(3, target.Calc.add(1, 2));
    });
  });
  describe('#mul()', function () {
    it('should mul 1 and 2', function () {
      assert.equal(2, target.Calc.mul(1, 2));
    });
  });
});

