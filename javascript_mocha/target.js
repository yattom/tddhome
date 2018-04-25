exports.items = {
  1: { name: 'Apple', price: 100 },
  2: { name: 'Mikan', price: 40 },
  3: { name: 'Grape', price: 150 },
  4: { name: 'Nori Bento', price: 350 },
  5: { name: 'Shake Bento', price: 400 },
  6: { name: 'Tobacco', price: 420, tax_included: true },
  7: { name: 'Menthol Tobacco', price: 440, tax_included: true },
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

  discounted_items() {
    let discounted_items = [];
    for(let i = 0; i < this.items.length; i++) {
      const item = this.items[i].item;
      const amount = this.items[i].amount;
      if(item.name == 'Apple') {
        discounted_items.push({ item: { name: "3 Apples", price: 280 }, amount: Math.floor(amount / 3) } );
        discounted_items.push({ item: item, amount: amount % 3 } );
      } else if(amount >= 11) {
        discounted_items.push({ item: item, amount: amount - Math.floor(amount / 11) } );
      } else {
        discounted_items.push(this.items[i]);
      }
    }
    return discounted_items;
  }

  total() {
    let sum = 0;
    let sum_for_tax = 0;
    let discounted_items = this.discounted_items();
    for(let i = 0; i < discounted_items.length; i++) {
      sum += discounted_items[i].item.price * discounted_items[i].amount;
      if(!discounted_items[i].item.tax_included) {
        sum_for_tax += discounted_items[i].item.price * discounted_items[i].amount;
      }
    }
    const tax = Math.floor(sum_for_tax * 0.08);
    return { total: sum, including_tax: sum + tax };
  }
};
exports.Receipt = Receipt;
