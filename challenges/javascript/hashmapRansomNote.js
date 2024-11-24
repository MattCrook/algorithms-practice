/*
-----------------------------------------------
Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

-----------------------------------------------
*/

//---------------------------------//
// Solution 1
//
// Complexity
//   - Time complexity: O(m+n)
//   - m: the length of magazine.
//   - n: the length of ransomNote.
//
// Space complexity:
//   - O(26) → O(1)
//---------------------------------//
function canConstruct(ransomNote, magazine) {
  let magazineHash = {};

  for (let c of magazine) {
    magazineHash[c] = (magazineHash[c] || 0) + 1;
  }

  for (let c of ransomNote) {
    if (!magazineHash[c] || magazineHash[c] <= 0) {
      return false;
    }
    magazineHash[c]--;
  }

  return true;
}

console.log(canConstruct("a", "b"));
console.log(canConstruct("aa", "ab"));
console.log(canConstruct("aa", "aab"));
console.log("--------------------------");

//---------------------------------//
// Solution 2

// Complexity
//  - Time complexity: O(k∗(m+n)),
//   - k: the number of unique characters in ransomNote.
//   - m: the length of magazine.
//   - n: the length of ransomNote.
//  - Space complexity: O(26) → O(1)
// This is similar to solution 1. We take unique characters of ransomNote and count them in magazine.
//  - To get unique characters of ransomNote, we use set.
//---------------------------------//

function canConstruct2(ransomNote, magazine) {
  if (ransomNote.length > magazine.length) {
    return false;
  }

  for (const c of new Set(ransomNote)) {
    if (magazine.split(c).length - 1 < ransomNote.split(c).length - 1) {
      return false;
    }
  }

  return true;
}

console.log(canConstruct2("a", "b"));
console.log(canConstruct2("aa", "ab"));
console.log(canConstruct2("aa", "aab"));
console.log("--------------------------");

//---------------------------------//
// Using the alphabet (26 letters)
//JavaScript Code
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
//---------------------------------//
var canConstruct3 = function (ransomNote, magazine) {
  const arr = new Array(26).fill(0);
  for (let i = 0; i < magazine.length; i++) arr[magazine.charCodeAt(i) - 97]++;

  for (let i = 0; i < ransomNote.length; i++) {
    const arrIdx = ransomNote.charCodeAt(i) - 97;
    if (arr[arrIdx] === 0) return false;
    arr[arrIdx]--;
  }

  return true;
};

console.log(canConstruct3("a", "b"));
console.log(canConstruct3("aa", "ab"));
console.log(canConstruct3("aa", "aab"));
console.log("--------------------------");

//---------------------------------//
// Simple Solution
//---------------------------------//
const canConstructSimple = (ransomNote, magazine) => {
  for (const character of magazine) {
    ransomNote = ransomNote.replace(character, "");
  }

  if (!ransomNote) return true;
  else return false;
};

console.log(canConstructSimple("a", "b"));
console.log(canConstructSimple("aa", "ab"));
console.log(canConstructSimple("aa", "aab"));
console.log("--------------------------");
