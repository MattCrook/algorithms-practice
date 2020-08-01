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
