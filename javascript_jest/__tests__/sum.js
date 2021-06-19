const sum = require('../sum')

test('足し算：1 + 2 = 3', () => {
    expect(sum(1, 2)).toBe(3);
});
