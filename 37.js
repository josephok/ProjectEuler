// Truncatable primes
// Problem 37
//
// The number 3797 has an interesting property. Being prime itself, it is
// possible to continuously remove digits from left to right, and remain prime
// at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
// left: 3797, 379, 37, and 3.
//
// Find the sum of the only eleven primes that are both truncatable from left
// to
// right and right to left.
//
// NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
//
// Answer:
// 748317

"use strict";

class TruncatablePrimes {
    static isPrime(n) {
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;
        if (n % 2 == 0 || n % 3 == 0)
            return false;
        let r = Math.floor(Math.sqrt(n));
        let f = 5;
        while (f <= r) {
            if (n % f == 0 || n % (f+2) == 0)
                return false;
            f += 6;
        }
        return true;
    }

    static isTrunc(n) {
        for (let d=1; d<n.toString().length; d++) {
            if (!this.isPrime(n.toString().substring(d)) ||
                !this.isPrime(n.toString().substring(0, d)))
                return false;
        }
        return true;
    }

    static output() {
        var n = 11, f = 1;
        var tp = [];
        while (tp.length < 11) {
            n += 3 - f;
            f = -f;
            if (!(n > 100 && n.toString().match(/[245680]/))) {
                if (this.isPrime(n) && this.isTrunc(n))
                    tp.push(n);
            }
        }

        console.log(tp.reduce((prev, curr) => prev + curr));
    }
}

TruncatablePrimes.output();
