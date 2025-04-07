import { add } from './calculator';

describe('calculator', () => {
    test('add', () => {
        expect(add(2, 3)).toBe(5);
    })
})