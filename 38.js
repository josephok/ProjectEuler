// Pandigital multiples
// Problem 38
//
// Take the number 192 and multiply it by each of 1, 2, and 3:
//
// 192 × 1 = 192
// 192 × 2 = 384
// 192 × 3 = 576
// By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
//
// The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
//
// What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

// Answer:
// 932718654

"use strict";

class PandigitalMultiples {
    static arraysEqual(arr1, arr2) {
        if(arr1.length !== arr2.length)
            return false;
        for(var i = arr1.length; i--;) {
            if(arr1[i] !== arr2[i])
                return false;
        }

        return true;
    }

    static isPandigital(str) {
        let digits = str.split("").sort();
        if (this.arraysEqual(digits, ['1', '2', '3', '4', '5', '6', '7', '8', '9']))
            return true;
        else
            return false;
    }

    static output() {
        let result = 0;
        for (let i = 9387; i >= 9234; i--) {
            result = String.prototype.concat(i, 2*i);
            if (this.isPandigital(result)) {
                console.log(result);
                return result;
            }
        }
    }
}

PandigitalMultiples.output();
