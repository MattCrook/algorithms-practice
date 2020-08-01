// Given an array of numbers, find all the odd numbers. Negatives do not count.


const array = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
const array_2 = [ 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1 ]
function findOdd(array) {
    const odds = [];
    array.map(n => {
        if ((n % 2 !== 0) && (n > 0)) {
            odds.push(n);
        }
    })
    return odds.length;
}
console.log(findOdd(array))

function findOdd2(array) { 
    const odds = array.filter(n => n % 2 !== 0 && n > 0);
    return odds.length;
}
console.log(findOdd2(array_2))
