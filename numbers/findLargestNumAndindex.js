// Find the largest number in the array and return the number and its index.
stockPrices = [10, 7, 5, 8, 11, 9];

function getMaxProfit(arr) {
  let maxNum = Math.max(...arr);
  for (i in arr) {
    let value = arr[i];
    let index = i;
    if (value === maxNum) console.log(index, value);
  }
}

getMaxProfit("{stockPrices}", getMaxProfit(stockPrices));
console.log("----------------");

const solution = (arr) => {
  let sol = {};
  const largestNumber = Math.max(...arr);
  for (n in arr) {
    let value = arr[n];
    let index = n;
    if (value === largestNumber) {
      sol["index"] = index;
      sol["value"] = value;
    }
  }
  return sol;
};

console.log(solution(stockPrices));
console.log("----------------");

const findLargestNumber = (arr) => {
  const largestNum = Math.max(...arr);
  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] === largestNum) {
      console.log({ index: i, value: arr[i] });
    }
  }
};

console.log(solution(stockPrices));
