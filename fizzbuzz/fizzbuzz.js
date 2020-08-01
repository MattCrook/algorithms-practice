// The classic, from 0 to 100, print out fizz for all numbers divisible by 3, buzz for numbers divisible by 5, and fizzbuzz for numbers divisible by 15.
// For all others, print out the number.


function fizzbuzz() {
  for (let i = 0; i < 100; i++) {
    if (i % 15 === 0) {
      console.log("fizzbuzz");
    } else if (i % 5 === 0) {
      console.log("buzz");
    } else if (i % 3 === 0) {
      console.log("fizz");
    } else {
      console.log(i);
    }
  }
}
fizzbuzz();

// To get shorthand and fancy...
for (let i = 0; i < 100; ) console.log((++i % 3 ? "" : "fizz") + (i % 5 ? "" : "buzz") || i);
