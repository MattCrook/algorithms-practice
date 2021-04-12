// Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted,
// compares each pair of adjacent items and swaps them if they are in the wrong order (ascending or descending arrangement).
// The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

let arr = [1, 4, 6, 2, 6, 7, 10]

const bubbleSort = (inputArr) => {
    let len = inputArr.length;
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            if (inputArr[j] > inputArr[j + 1]) {
                let tmp = inputArr[j];
                inputArr[j] = inputArr[j + 1];
                inputArr[j + 1] = tmp;
            }
        }
    }
    return inputArr;
};


console.log(bubbleSort(arr));

// Using a do/ while loop
const bubbleSortDoWhile = (inputArr) => {
    let len = inputArr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 0; i < len; i++) {
            if (inputArr[i] > inputArr[i + 1]) {
                let tmp = inputArr[i];
                inputArr[i] = inputArr[i + 1];
                inputArr[i + 1] = tmp;
                swapped = true;
            }
        }
    } while (swapped);
    return inputArr;
};

// Practical ES6 way using the sort method
const bubbleSortArrayMethod = (arr) => {
    arr.sort((a, b) => a - b);
    return arr;
}
console.log(bubbleSortArrayMethod(arr));
