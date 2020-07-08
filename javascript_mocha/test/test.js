var assert = require('assert');
var target = require('../target');

describe('Calc', function() {
    describe('#add()', function() {
        it('should add 1 and 2', function() {
            assert.equal(3, target.Calc.add(1, 2));
        });
    });
    describe('#mul()', function() {
        it('should mul 1 and 2', function() {
            assert.equal(2, target.Calc.mul(1, 2));
        });
    });
    describe('#sub()', function() {
        it('should calculate 3 - 2', function() {
            assert.equal(1, target.Calc.sub(3, 2));
        });
        it('should calculate 6 - 3', function() {
            assert.equal(3, target.Calc.sub(6, 3));
        });
        describe('#sub() 負の整数', function() {
            it('should calculate 1 - 2', function() {
                assert.equal(-1, target.Calc.sub(1, 2));
            });
        });
    })
    describe('#div()', function() {
        it('should calculate 4 わる 2', function() {
            assert.strictEqual('2', target.Calc.div(4, 2));
        });
        it('should calculate 3 わる 2', function() {
            assert.equal('1 あまり 1', target.Calc.div(3, 2));
        });
        it('should mod 3 わる 2', function() {
            assert.equal(' あまり 1', target.Calc.mod(3, 2));
        });
        it('should mod 4 わる 2', function() {
            assert.equal('', target.Calc.mod(4, 2));
        });
        it('should calculate 2 わる 0', function() {
            assert.equal('0 では われません', target.Calc.div(2, 0));
        });
        it('should calculate -5 わる 2', function() {
            assert.equal('-2 あまり -1', target.Calc.div(-5, 2));
        });
    });
});