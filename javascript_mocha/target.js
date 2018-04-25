exports.items = {
  1: { name: 'Apple', price: 100 },
  2: { name: 'Mikan', price: 40 },
  3: { name: 'Grape', price: 150 },
  4: { name: 'Nori Bento', price: 350 },
  5: { name: 'Shake Bento', price: 400 },
  6: { name: 'Tobacco', price: 420 },
  7: { name: 'Menthol Tobacco', price: 440 },
  8: { name: 'Lighter', price: 100 },
  9: { name: 'Tea', price: 80 },
  10: { name:  'Coffee', price: 100 },
};

class Receipt {
  constructor() {
    this.items = [];
  }

  add(item, amount) {
    this.items.push({ item: item, amount: amount });
  }

  total() {
    let sum = 0;
    for(let i = 0; i < this.items.length; i++) {
      sum += this.items[i].item.price * this.items[i].amount;
    }
    return sum;
  }

  total_including_tax() {
    return Math.floor(this.total() * 1.08);
  }
};
exports.Receipt = Receipt;
