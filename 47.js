// Distinct primes factors
// Problem 47
//
// The first two consecutive numbers to have two distinct prime factors are:
//
// 14 = 2 × 7
// 15 = 3 × 5
//
// The first three consecutive numbers to have three distinct prime factors are:
//
// 644 = 2² × 7 × 23
// 645 = 3 × 5 × 43
// 646 = 2 × 17 × 19.
//
// Find the first four consecutive integers to have four distinct prime factors.
// What is the first of these numbers?
//
//Answer:
// 134043

"use strict";

class DistinctPrimesFactors {
    static factor(n) {
        let f = 1;
        let factors = [];
        let prime_gaps = [2, 4, 2, 4, 6, 2, 6, 4];
        let e = 0;
        var gaps = [];
        if (n < 1) {
            return [];
        }

        while (true) {
            if (f < 11) {
                gaps = [1, 1, 2, 2, 4];
            }
            else {
                gaps = prime_gaps;
            }
            for (let gap of gaps) {
                f += gap;
                if (f * f > n) {
                    if (n === 1) {
                        return factors;
                    }
                    else {
                        factors.push([n, 1]);
                        return factors;
                    }
                }

                if ((n % f) == 0) {
                    e = 1;
                    n = Math.floor(n / f);
                    while ((n % f) == 0) {
                        n = Math.floor(n / f);
                        e++;
                    }
                    factors.push([f, e])
                }
            }
        }
    }

    static output() {
        let ci = 1;
        let nf = 4;
        let ns = 4;
        let n = 2 * 3 * 5 * 7;
        while (ci != ns) {
            n++;
            if (this.factor(n).length == nf) {
                ci++;
            }
            else {
                ci = 0;
            }
        }

        console.log(n - nf + 1);
    }
}

DistinctPrimesFactors.output();
