function hello() {
  return "Hello, World!";
}

class Button {
  constructor(vm, beverage, unit_price) {
    this.vm = vm;
    this.beverage = beverage;
    this.unit_price = unit_price;
  }

  available() {
    return this.vm.amount >= this.unit_price;
  }

  is_lit() { 
    return this.available();
  }

  push() {
    if (this.available()) {
      this.vm.dispense(this.beverage);
    }
  }
}

class VendingMachine {

  constructor() {
    this.bucket = null;
    this.amount = 0;
    this.buttons = {
      コーラ: new Button(this, 'コーラ', 100),
      ウーロン茶: new Button(this, 'ウーロン茶', 100),
      レッドブル: new Button(this, 'レッドブル', 200),
    };
  }

  take() {
    return this.bucket;
  }

  insert100() {
    this.amount += 100;
  }

  get_button(beverage) {
    if (this.buttons[beverage] == undefined) {
      throw "Undefined Beverage :" + beverage;
    }
    return this.buttons[beverage];
  }

  dispense(beverage) {
    this.bucket = beverage;
  }
}
/*
function add(x, y) {
  return x + y;
}

function sub(x, y) {
  return x - y;
}
*/