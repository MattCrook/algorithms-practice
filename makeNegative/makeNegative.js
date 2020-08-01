// Make a given number negative.

function makeNegative(num) {
  return num < 0 ? num : -num;
}
console.log("{makeNegative}", makeNegative(5));

function makeNegativeIfs(num) {
  if (num < 0) {
    return num;
  } else if (num > 0) {
    return -num;
  } else {
    return 0;
  }
}
console.log("{makeNegativeIfs}", makeNegativeIfs(0));
