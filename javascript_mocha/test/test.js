// TDD traial for https://gist.github.com/yattom/c906216ab1fdf68a133ba0fbade1a395
var assert = require('assert');
var items = require('../target').items;

function assert_item(item, name, price) {
  assert.equal(item.name, name);
  assert.equal(item.price, price);
}
describe('defined items', function() {
  describe('has right name and price', function() {
    it('for 10 items', function() {
      assert_item(items[1], 'Apple', 100);
      assert_item(items[2], 'Mikan', 40);
      assert_item(items[3], 'Grape', 150);
      assert_item(items[4], 'Nori Bento', 350);
      assert_item(items[5], 'Shake Bento', 400);
      assert_item(items[6], 'Tobacco', 420);
      assert_item(items[7], 'Menthol Tobacco', 440);
      assert_item(items[8], 'Lighter', 100);
      assert_item(items[9], 'Tea', 80);
      assert_item(items[10], 'Coffee', 100);
    });
  });
});

