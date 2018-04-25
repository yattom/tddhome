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
      assert.equal(receipt.total().total, 100);
    });
    it('3 of same item', function() {
      var receipt = new Receipt();
      receipt.add(items[2], 3);
      assert.equal(receipt.total().total, 120);
    });
    it('several items', function() {
      var receipt = new Receipt();
      receipt.add(items[1], 2);
      receipt.add(items[2], 2);
      receipt.add(items[3], 1);
      assert.equal(receipt.total().total, 100 * 2 + 40 * 2 + 150);
    });
  });
});

describe('total price including tax', function() {
  describe('simply add up', function() {
    it('only 1 item', function() {
      var receipt = new Receipt();
      receipt.add(items[1], 1);
      assert.equal(receipt.total().including_tax, 108);
    });
    it('3 of same item', function() {
      var receipt = new Receipt();
      receipt.add(items[2], 3);
      assert.equal(receipt.total().including_tax, 129);
    });
    it('several items', function() {
      var receipt = new Receipt();
      receipt.add(items[1], 2);
      receipt.add(items[2], 2);
      receipt.add(items[3], 1);
      assert.equal(receipt.total().including_tax, Math.floor((100 * 2 + 40 * 2 + 150) * 1.08));
    });
    describe("price of tobbaco includes tax already", function() {
      it("single tobbaco", function() {
        var receipt = new Receipt();
        receipt.add(items[6], 1);
        assert.equal(receipt.total().including_tax, 420);
      });
    });
  });
});

describe("discount when buying many", function() {
  describe('discount for Apple', function() {
    it("3 Apples are discounted", function() {
      var receipt = new Receipt();
      receipt.add(items[1], 3);
      assert.equal(receipt.total().total, 280);
    });
    it("discounted apples have tax", function() {
      var receipt = new Receipt();
      receipt.add(items[1], 3);
      assert.equal(receipt.total().including_tax, Math.floor(280 * 1.08));
    });
    it("6 Apples are discounted", function() {
      var receipt = new Receipt();
      receipt.add(items[1], 3 * 2);
      assert.equal(receipt.total().total, 280 * 2);
    });
    it("6 of 7 Apples are discounted", function() {
      var receipt = new Receipt();
      receipt.add(items[1], 3 * 2 + 1);
      assert.equal(receipt.total().total, 280 * 2 + 100);
    });
  });
});
