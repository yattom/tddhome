import {fizzbuzz} from './fizzbuzz';

describe("FizzBuzz", () => {
    describe("数を数の文字列に変換する", () => {

        test("1ならば1が返ってくる", () => {
            expect(fizzbuzz(1)).toBe("1");
        })
    })
    describe("3の倍数の場合はFizzに変換する", () => {

        test("3ならばFizzが返ってくる", () => {
            expect(fizzbuzz(3)).toBe("Fizz");
        })

    })
    describe("5の倍数の場合はBuzzに変換する", () => {
        test("5ならばBuzzが返ってくる", () => {
            expect(fizzbuzz(5)).toBe("Buzz");
        })
    })
    describe("3と5の倍数の場合はFizzBuzzに変換する", () => {
        test("15ならばFizzBuzzが返ってくる変換する", () => {
            expect(fizzbuzz(15)).toBe("FizzBuzz");
        })
    })
})