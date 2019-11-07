/*
 * DAILY CODING CHALLENGE
 *
 * DATE: 11/06/19
 *
 * CHALLENGE: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
 *
 *            E.G.: Given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
 *
*/

function isSum(list, k) {

    const map = new Map()

    for (let i = 0; i < list.length; i++) {
        map.set(list[i], i);
    }

    for (let i = 0; i < list.length; i++) {
        const difference = k - list[i];
        if (map.has(difference) && map.get(difference) != i) return true;
    }
}

/*
 * TESTING
 *
 * BREAKDOWN: Iterate through a map consisting of 100 (list, k) test cases,
 *            where a list will consist of 20 random numbers between
 *            1 - 20 (inclusive) and k is a random number between
 *            1 - 40 (inclusive).
 *
*/

const map  = new Map();
const k    = Math.floor(Math.random() * 40) + 1;
let   i    = 0;

for (let i = 0; i < 100; i++) {
    map.set(Array.from({length: 10}, () => Math.floor(Math.random() * 20) + 1), k);
}

map.forEach( function (k, list) {
    const answer = isSum(list, k);
    if (answer === undefined) console.log(`${++i})`.padEnd(5) + `list = ${list}`.padEnd(37) + `k = ${k}, answer = ❌`);
    else                      console.log(`${++i})`.padEnd(5) + `list = ${list}`.padEnd(37) + `k = ${k}, answer = ✅`);
});
