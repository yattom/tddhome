// TDD traial for https://gist.github.com/yattom/c906216ab1fdf68a133ba0fbade1a395
var assert = require('assert');
var items = require('../target').items;

function assert_item(item, name, price) {
  assert.equal(item.name, name);
  assert.equal(item.price, price);
}
describe('defined items', function() {
  describe('has right name and price', function() {
    it('for Apple', function() {
      assert_item(items[1], 'Apple', 100);
    });
  });
});

