//-----------------------------------------------------------------------//
// Longest Common Prefix
//
// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
//
//
// Example 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"
//
// Example 2:
// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
//-----------------------------------------------------------------------//

const strings1 = ["flower", "flow", "flight"];
const strings2 = ["dog", "racecar", "car"];

//------------------------------------//
// Kind of simple solution, however not super efficient. (complexity too high)
// More of a brute force way to solve.
//------------------------------------//
function longestCommonPrefix(strings) {
  if (strings.length == 0) {
    return "";
  }

  let base = strings[0];
  let baseLength = Array.from(base).length;

  for (let i = 0; i < baseLength; i++) {
    for (let j = 1; j < strings.length; j++) {
      if (i == j.length || j[i] != base[i]) {
        return base;

    //for (let j = 0; j < strings.slice(1).length; j++) {
      //if (i == strings.slice(1)[j].length || Array.from(strings.slice(1)[j])[j] != base[i]) {
        //return base.slice(0, i);
        //return base;
      }
    }
  }
  return base
}

console.log("longestCommonPrefix", longestCommonPrefix(strings1));
console.log("longestCommonPrefix", longestCommonPrefix(strings2));
console.log("--------------------------------");

//------------------------------------//
// Slightly more efficient solution, slightly less complexity.
//------------------------------------//
const longestCommonPrefixInStrings = (strings) => {
  let prefix = strings[0];
  let prefixLength = prefix.length;

  for (let i = 1; i < strings.length; i++) {
    let s = strings[i];
    while (prefix !== s.substring(0, prefixLength)) {
      prefixLength--;
      if (prefixLength === 0) {
        return "";
      }
      prefix = prefix.substring(0, prefixLength);
    }
  }

  return prefix;
};

console.log("longestCommonPrefixInStrings", longestCommonPrefixInStrings(strings1));
console.log("longestCommonPrefixInStrings", longestCommonPrefixInStrings(strings2));
console.log("--------------------------------");

//------------------------------------//
/**
 * @param {string[]} strs
 * @return {string}
 */
// Most efficient solution, with the lowest complexity of these three solutions.
//------------------------------------//
function longestCommonPrefix03(strings) {
  strings.sort();
  let a = strings[0];
  let b = strings[strings.length - 1];
  let c = "";
  for (let i = 0; i < a.length; i++) {
    if (a[i] == b[i]) {
      c += a[i];
    } else {
      break;
    }
  }
  return c;
};

console.log("longestCommonPrefix03", longestCommonPrefix03(strings1));
console.log("longestCommonPrefix03", longestCommonPrefix03(strings2));
console.log("--------------------------------");
