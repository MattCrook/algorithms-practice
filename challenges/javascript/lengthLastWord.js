//#######################################################
// Length of Last Word

// Given a string s consisting of words and spaces, return the length of the last word in the string.
// A word is a maximal substring consisting of non-space characters only.

// Example 1:
// Input: s = "Hello World"
// Output: 5
// Explanation: The last word is "World" with length 5.

// Example 2:
// Input: s = "   fly me   to   the moon  "
// Output: 4
// Explanation: The last word is "moon" with length 4.

// Example 3:
// Input: s = "luffy is still joyboy"
// Output: 6
// Explanation: The last word is "joyboy" with length 6.
//########################################################

const lengthOfLastWord = (s) => {
  // remove leading and trailing whitespace and 
  // split a string into substrings using the specified separator and return them as an array.
  const words = s.trim().split(" ");
  const lastWord = words[words.length - 1];
  // return last word, split each letter into strings in an array and return length of array.
  return lastWord.split("").length;
};

console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord("   fly me   to   the moon  "));
console.log(lengthOfLastWord("luffy is still joyboy"));
console.log("---------------------");

function lengthOfLastWord2(s) {
  s = s.trim();

  let length = 0;
  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] !== " ") {
      length++;
    } else if (length > 0) {
      break;
    }
  }

  return length;
}

console.log(lengthOfLastWord2("Hello World"));
console.log(lengthOfLastWord2("   fly me   to   the moon  "));
console.log(lengthOfLastWord2("luffy is still joyboy"));
console.log("---------------------");

/*
Time complexity: O(n)
Space complexity: O(1)
*/
var lengthOfLastWord3 = function (s) {
  let end = s.length - 1;

  while (end >= 0 && s[end] === " ") {
    end--;
  }

  let start = end;
  while (start >= 0 && s[start] !== " ") {
    start--;
  }

  return end - start;
};

console.log(lengthOfLastWord3("Hello World"));
console.log(lengthOfLastWord3("   fly me   to   the moon  "));
console.log(lengthOfLastWord3("luffy is still joyboy"));
console.log("---------------------");

/*
Initialize Variables: Prepare length and counting for tracking.
Loop Through Characters: Examine each character to determine if it's part of a word or a space.
Update Length: Adjust length based on whether you're starting a new word or continuing an existing one.
Handle Spaces: Reset counting when spaces are encountered.
Return Result: Output the length of the last word.
This approach ensures that only the length of the last word is calculated, and any trailing spaces or spaces between words do not affect the final result.
*/
var lengthOfLastWord4 = function (s) {
  let length = 0;
  let counting = false;

  for (let c of s) {
    if (c !== " ") {
      if (!counting) {
        counting = true;
        length = 1;
      } else {
        length++;
      }
    } else {
      counting = false;
    }
  }

  return length;
};

console.log(lengthOfLastWord4("Hello World"));
console.log(lengthOfLastWord4("   fly me   to   the moon  "));
console.log(lengthOfLastWord4("luffy is still joyboy"));
console.log("---------------------");
