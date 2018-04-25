// TDD traial for https://gist.github.com/yattom/c906216ab1fdf68a133ba0fbade1a395
var assert = require('assert');
var items = require('../target').items;

describe('defined items', function() {
  describe('has right unit price', function() {
    it('for Apple', function() {
      assert.equal(items[1].name, 'Apple');
    });
  });
});

