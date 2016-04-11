// Champernowne's constant
// Problem 40
//
// An irrational decimal fraction is created by concatenating the positive integers:
//
// 0.123456789101112131415161718192021...
//
// It can be seen that the 12th digit of the fractional part is 1.
//
// If dn represents the nth digit of the fractional part, find the value of the following expression.
//
// d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
//
// Answer:
// 210

"use strict";

class ChampernownesConstant {
    static d(n) {
        let size = 0;
        while (n > (size + 1) * 9 * Math.pow(10, size)) {
            n -= (size + 1) * 9 * Math.pow(10, size);
    		size++;
        }
        let j = Math.floor((n - 1) / (size + 1));
        let k = (n - 1) % (size + 1);
        return parseInt((Math.pow(10, size) + j).toString()[k]);
    }

    static output() {
        let result = 1;
        for (let i = 0; i < 7; i++) {
            result *= this.d(Math.pow(10, i));
        }
        console.log(result);
    }
}

ChampernownesConstant.output();
