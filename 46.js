// Goldbach's other conjecture
// Problem 46
// It was proposed by Christian Goldbach that every odd composite number can be
// written as the sum of a prime and twice a square.
//
// 9 = 7 + 2×12
// 15 = 7 + 2×22
// 21 = 3 + 2×32
// 25 = 7 + 2×32
// 27 = 19 + 2×22
// 33 = 31 + 2×12
//
// It turns out that the conjecture was false.
//
// What is the smallest odd composite that cannot be written as the sum of a
// prime and twice a square?
//
// Answer:
// 5777
//
"use strict";

var _ = require('underscore');

class Goldbach {
    static output() {
        let n = 5;
        let f = 1;
        let primes = new Set();
        while (true) {
            if (Array.from(primes).every((i) => n % i)) {
                primes.add(n);
            }
            else {
                let a = _.range(1, n);
                if (!(a.some((i) => primes.has(n-2*i*i)))) {
                    break;
                }
            }

            n += 3-f;
            f = -f;
        }

        return console.log(n);
    }
}

Goldbach.output();
