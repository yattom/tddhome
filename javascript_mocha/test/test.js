// TDD traial for https://gist.github.com/yattom/c906216ab1fdf68a133ba0fbade1a395
const assert = require('assert');
const items = require('../target').items;
const Receipt = require('../target').Receipt;

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

describe('total price', function() {
  describe('simply add up', function() {
    it('only 1 item', function() {
      var receipt = new Receipt();
      receipt.add(items[1], 1);
      assert.equal(receipt.total(), 100);
    });
  });
});
