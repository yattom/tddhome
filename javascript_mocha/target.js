const Calc = {
    add: function(a, b) { return a + b; },
    mul: function(a, b) { return a * b; },
    sub: function(a, b) { return a - b; },
    div: function(a, b) {
        if (b === 0) {
            return '0 では われません';
        }
        return `${a / b | 0}${Calc.mod(a, b)}`;
    },
    mod: function(a, b) {
        const ans = a % b;
        if (ans === 0) {
            return '';
        }
        return ` あまり ${ans}`;
    }
};

module.exports = { Calc: Calc };