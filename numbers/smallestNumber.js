// Smallest number out of 2 integers

function getMin(num1, num2) {
  return Math.min(num1, num2);
}
console.log(getMin(4, 9));

function getMinSecond(a, b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
}
console.log(getMinSecond(9, 8));
