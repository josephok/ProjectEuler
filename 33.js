// The fraction 49/98 is a curious fraction, as an inexperienced mathematician
// in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
// is correct, is obtained by cancelling the 9s.
// We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
// There are exactly four non-trivial examples of this type of fraction, less
// than one in value, and containing two digits in the numerator and
// denominator. If the product of these four fractions is given in its lowest
// common terms, find the value of the denominator.

"use strict";

let d = 1;
for (let i=1; i<10; i++) {
    for (let j=1; j<i; j++) {
        let q = Math.floor((9*j*i) / (10*j - i));
        let r = (9*j*i) % (10*j - i);
        if (!r && q <= 9)
        d *= i / j;
    }
}

console.log(d)
