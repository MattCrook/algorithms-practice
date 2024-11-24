//##########################################################//
// Valid Palindrome

// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
// it reads the same forward and backward. Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.
//#########################################################//

const testStr1 = "A man, a plan, a canal, Panama";
const testStr2 = "race a car";
const testStr3 = "No 'x' in Nixon";
const testStr4 = "";

//-----------------------------------//
/*
Solution 1:
can implement a function that checks if the string reads the same forward and backward, ignoring spaces, punctuation, and letter case.

1 .Normalize the string: Remove all non-alphanumeric characters (e.g., spaces, punctuation) and convert the string to lowercase so the comparison is case-insensitive.
2 .Check if the string is the same forwards and backwards: Compare the normalized string with its reverse.

Explanation
  - str.replace(/[^A-Za-z0-9]/g, ''): This regular expression removes all characters that are not letters or numbers.It uses[^ A - Za - z0 - 9] to match any non - alphanumeric character and removes them globally(the g flag).
  - toLowerCase(): This ensures that the comparison is case-insensitive.
  - split('').reverse().join(''): This method splits the string into an array of characters, reverses the array, and joins it back into a string.
  - cleanedStr === reversedStr: Finally, we compare the cleaned version of the string with its reversed version.

Time Complexity:
  - Time Complexity: O(n), where n is the length of the input string. We iterate over the string once to clean it, and once more to reverse it.
  - Space Complexity: O(n), because we store a cleaned version of the string and its reverse.
*/
//------------------------------------//
function isPalindrome1(str) {
  // Remove non-alphanumeric characters and convert to lowercase
  const cleanedStr = str.replace(/[^A-Za-z0-9]/g, "").toLowerCase();

  // Compare the cleaned string with its reverse
  const reversedStr = cleanedStr.split("").reverse().join("");
  return cleanedStr === reversedStr;
}

const testString1 = "A man, a plan, a canal, Panama";
const testString2 = "race a car";

console.log(isPalindrome1(testStr1)); // true
console.log(isPalindrome1(testStr2)); // false
console.log(isPalindrome1(testStr3)); // false
console.log(isPalindrome1(testStr4)); // false

console.log("------------------------------");

//-----------------------------------------//
/*
Using Two Pointers

Instead of creating a new cleaned string or reversing it, we will:
  -Use two pointers, one starting from the beginning of the string (left) and one starting from the end of the string (right).
  -Skip non-alphanumeric characters using the left and right pointers.
  -If we encounter a character that isn't alphanumeric, we move the corresponding pointer inward.
  -Compare characters at the left and right pointers. If they don't match, return false.
  -If we reach the middle of the string without any mismatches, return true.
*/
//-----------------------------------------//
const isPalindrome2 = (str) => {
  let left = 0;
  let right = str.length - 1;

  while (left < right) {
    // Skip non-alphanumeric characters from the left side
    if (!isAlphanumeric(str[left])) {
      left++;
      continue;
    }
    // Skip non-alphanumeric characters from the right side
    if (!isAlphanumeric(str[right])) {
      right--;
      continue;
    }

    // Compare characters at the left and right pointers
    if (str[left].toLowerCase() !== str[right].toLowerCase()) {
      return false; // Characters don't match
    }

    // Move the pointers closer to the center
    left++;
    right--;
  }

  return true; // All characters match
};

// Helper function to check if a character is alphanumeric
const isAlphanumeric = (char) => {
  return /^[A-Za-z0-9]$/.test(char);
}

console.log(isPalindrome2(testStr1));
console.log(isPalindrome2(testStr2));
console.log(isPalindrome2(testStr3));
console.log(isPalindrome2(testStr4));
console.log("------------------------------");

/*
//----------------------------------//
 Using Recursion (and Memoization)

Expect the calculations to have to perform repeat operations. (like finding "aba" multiple times,)
  - Memoization can be a good solution to fetch results that have already been calculated.

Abstracted out helper functions:
  - Helper function (preprocessHelper) to process the string by filtering out non-alphanumeric characters.
  - Recursive helper function (check) to check palindrome

Preprocessing:
  - The preprocessHelper function converts the string to lowercase and removes all non-alphanumeric characters using a regular expression (/[^a-z0-9]/g).
Recursive Check:
  - The checkHelper function compares the characters at the left and right indices.
  - If they match, it recursively checks the substring between these indices.
  - If the characters do not match at any point, it immediately returns false.
  - The recursion continues until the left pointer meets or exceeds the right pointer, confirming that the string is a palindrome.

Solution:
- The string is first preprocessed to remove all non-alphanumeric characters and converted to lowercase.
- The recursive function then checks whether the string reads the same forward and backward by comparing characters from both ends, moving inward.

Space Complexity:
- The space complexity is O(n) due to the string created during preprocessing and the recursive call stack.
- This solution should work efficiently for strings of reasonable length.
*/
//-------------------------------//

// Using ES6 arrow function syntax just b/c...
const preprocessHelper = (string) => {
  const alphaNumericCharacters = string.toLowerCase().replace(/[^a-z0-9]/g, "");
  return alphaNumericCharacters;
};

const checkHelper = (input_string, left, right) => {
  if (left >= right) {
    return true;
  }

  const leftChar = input_string[left];
  const rightChar = input_string[right];

  if (leftChar !== rightChar) {
    return false;
  }

  return checkHelper(input_string, left + 1, right - 1);
};

const findPalindrome = (input_string) => {
  const processedString = preprocessHelper(input_string);
  return checkHelper(processedString, 0, processedString.length - 1);
};

console.log(findPalindrome(testStr1));
console.log(findPalindrome(testStr2));
console.log(findPalindrome(testStr3));
console.log(findPalindrome(testStr4));
console.log("------------------------------");
