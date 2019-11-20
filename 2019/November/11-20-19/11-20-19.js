/*
 * DAILY CODING CHALLENGE
 *
 * DATE: 11/20/19
 *
 * CHALLENGE: Given an array of integers, return a new array such that
 *            each element at index i of the new array is the product of
 *            all the numbers in the original array except the one at i.
 *
 *            E.G.: If our input was [1, 2, 3, 4, 5], the expected output
 *                  would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
 *                  the expected output would be [2, 3, 6].
 */

function products(array) {
    let productsArray = [];
    if (array.length >= 2) {
        for (let i = 0; i < array.length; i++) {
            productsArray.push(array.filter((x) => {return x !== array[i]}).reduce((a,b) => a * b));
        }
        return productsArray;
    } else {
        return "Please provide an array of size >= 2.";
    }
}

/*
 * TESTING
 *
 * BREAKDOWN: Pass 5 different arrays to products() and compare
 *            the expected results vs the actual results.
 *            If they are equal, the tests passes. Otherwise,
 *            it fails.
 */

 const data = [
     [1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]
 ]

 const expected = [
    [120,60,40,30,24],
    [5040,4320,3780,3360,3024],
    [32760,30030,27720,25740,24024],
    [116280,109440,103360,97920,93024],
    [303600,289800,277200,265650,255024]
 ]

function pass(expected, result) {
    if (expected.length !== result.length) return '❌';
    for (var i = 0; i < expected.length; i++) {if (expected[i] !== result[i]) return '❌';}
	return '✅';
};

for (let i = 0; i < 5; i++) {
    console.log(`${i+1}) ` + `Array = ${data[i]}`.padEnd(25)
                           + `Expected = ${expected[i]}`.padEnd(48)
                           + `Result = ${products(data[i])}`.padEnd(46)
                           + `Pass = ${pass(expected[i], products(data[i]))}`)
}
