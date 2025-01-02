// --------------------------------------------------------------------------- //
// Using one single line of JavaScript code, complete the following tasks on the array of integers below.
//
// 1. Sort the numbers in ascending and descending order: [13, 25, 6, 3, 11, 2, 18, 7, 21, 1, 29, 20, 12, 8]
//
// 2. Remove any integers greater than 19.
//
// 3. Multiply each remaining number by 1.5 and then subtract 1.
// 4.Then output (either in the DOM or the console) the sum of all the resulting numbers.
// --------------------------------------------------------------------------- //

const integers = [13, 25, 6, 3, 11, 2, 18, 7, 21, 1, 29, 20, 12, 8];

// ------ Sort Array Ascending ------ //
function sortAscending(array) {
  var sortedArray = array.sort((a, b) => a - b);
  return sortedArray;
}

console.log("sortAscending: ", sortAscending(integers));

// ------ Sort Array Descending ------ //
function sortDescending(array) {
  var sortedArray = array.sort((a, b) => a - b);
  return sortedArray.reverse();
}

console.log("sortDescending: ", sortDescending(integers));
console.log("---------------");

// ################################################################################### //

// ----------------- Remove all above 19: (MODIFYING ARRAY IN PLACE) --------------------- //
// Note - Iterate through the array IN REVERSE to avoid skipping elements after removal.
//  - Otherwise, loop will not work.
// ------------------------------------------------------------------------------------ //
function removeAllAboveNineteen(sortedArr) {
  for (let i = sortedArr.length - 1; i >= 0; i--) {
    const currentNum = sortedArr[i];
    if (currentNum > 19) {
      sortedArr.splice(i, 1);
    }
  }
  return sortedArr;
}
// Note - Array is already sorted here because previous function(s).
console.log("removeAllAboveNineteen", removeAllAboveNineteen(integers));
console.log("---------------");

// -------- Remove all above 19: (MODIFYING ARRAY IN PLACE) Using While Loop ----------------- //
// Can write this as passing in a sorted array (for example a pre sorted descending order array).
//   - Which will be an in place sorting, sorting original array.
//   - Did that in below example, creating a new array and using the sortDescending() function.
// Or, could also do it by passing in an unsorted array, creating new array and sorting it within the function and returning new array.
// ------------------------------------------------------------------------------------ //
function removeAllAboveNineteenWhileLoop(sortedArr) {
  let n = sortedArr[0];
  while (n > 19) {
    sortedArr.shift();
  }
  return sortedArr;
}

const unsortedIntegers = [13, 25, 6, 3, 11, 2, 18, 7, 21, 1, 29, 20, 12, 8];
sortDescending(unsortedIntegers);
console.log("removeAllAboveNineteenWhileLoop: ", removeAllAboveNineteenWhileLoop(integers));
console.log("---------------");

// -------- Remove all above 19: (RETURNING NEW ARRAY) ---------- //
// Returns a NEW ARRAY. The filter() method removes the given input and returns new array.
// Use the filter method to keep elements less than or equal to the given number.
// ---------------------------------------------------------- //
function removeAllAboveNineteenCreateNewArray(arr, num) {
  return arr.filter((element) => element <= num);
}

const integers_3 = [13, 25, 6, 3, 11, 2, 18, 7, 21, 1, 29, 20, 12, 8];
console.log("removeAllAboveNineteenCreateNewArray: ", removeAllAboveNineteenCreateNewArray(integers_3, 19));
console.log("---------------");

// ################################################################################### //

// -------- Multiply All Remaining by 1.5 and Then Subtract 1 ---------- //
function helper(number) {
  const multiply = number * 1.5;
  const subtract = multiply - 1;
  return subtract;
}

function multiplyAndSubtract(arr) {
  const newArr = [];
  for (let i = 0; i <= arr.length; i++) {
    const n = helper(arr[i]);
    newArr.push(n);
  }
  return newArr;
}

console.log("multiplyAndSubtract: ", multiplyAndSubtract(integers));
console.log("---------------");
