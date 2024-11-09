//--------------------------------------------------------//
// Write a function that takes in a list and shuffles it.
//--------------------------------------------------------//

//------- Modifies/ mutates original Array ---------//
function shuffleArray(array) {
  // loop through the array, in descending order
  // array.length == 6, so do - 1 b/c 0 index.
  for (let i = array.length - 1; i > 0; i--) {
    // using math.floor round integer down, so whole number.
    // and and math.random to return a random number
    // times the current iterator number plus 1.
    // grabs the current index, plus 1.
    let j = Math.floor(Math.random() * (i + 1));
    // saving off the index of "j" in the original array.
    let temp = array[i];
    // mutating the array, swapping the INDEX's, placing "j" in place of the current iterator.
    array[i] = array[j];
    // setting the new index, j, to the actual value of "temp".
    array[j] = temp;
  }
}

var arrayToShuffle = [1, 7, 9, 21, 25, 31];
shuffleArray(arrayToShuffle);
console.log("arrayToShuffle", arrayToShuffle);
console.log("--------------------------");



//------- Modifies/ mutates original Array ---------//
// Using ES6 function syntax
const shuffle = (array) => {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
};

const arrToShuffle = [1, "cat", 9, "dog", 25, 31];
console.log("originalArrToShuffle", arrToShuffle);
const s = shuffle(arrToShuffle);
// Logging out array again, b/c function mutates it in place.
console.log("Shuffle", arrToShuffle);
console.log("--------------------------");



//------- DOES NOT modify or mutate original Array ---------//
function shuffleNoMutate(array) {
  const tempArray = [...array];
  // Implement called the "Fisher-Yates shuffle"
  for (let i = tempArray.length - 1; i > 0; i--) {
    // Random index from 0 to i
    const j = Math.floor(Math.random() * (i + 1));
    let temp = tempArray[i];
    // Swap elements
    tempArray[i] = tempArray[j];
    tempArray[j] = temp;
    // or can do it in a one-liner
    // [tempArray[i], tempArray[j]] = [tempArray[j], tempArray[i]];
  }
  return tempArray;
}

const originArr = [1, "cat", 9, "dog", 25, "foo"];
const shuffleNoMutateArray = shuffleNoMutate(originArr);

console.log("OriginalArray", originArr);
console.log("shuffleNoMutateArray", shuffleNoMutateArray);
console.log("--------------------------");
