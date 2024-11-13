// Explanation
// str.replace(/[^A-Za-z0-9]/g, ''): This regular expression removes all characters that are not letters or numbers.It uses[^ A - Za - z0 - 9] to match any non - alphanumeric character and removes them globally(the g flag).
// toLowerCase(): This ensures that the comparison is case-insensitive.
// split('').reverse().join(''): This method splits the string into an array of characters, reverses the array, and joins it back into a string.
// cleanedStr === reversedStr: Finally, we compare the cleaned version of the string with its reversed version.

// Time Complexity:
// Time Complexity: O(n), where n is the length of the input string. We iterate over the string once to clean it, and once more to reverse it.
// Space Complexity: O(n), because we store a cleaned version of the string and its reverse.
function isPalindrome(str) {
  // Remove non-alphanumeric characters and convert to lowercase
  const cleanedStr = str.replace(/[^A-Za-z0-9]/g, "").toLowerCase();

  // Compare the cleaned string with its reverse
  const reversedStr = cleanedStr.split("").reverse().join("");
  return cleanedStr === reversedStr;
}

const testString1 = "A man, a plan, a canal, Panama";
const testString2 = "race a car";

console.log(isPalindrome(testString1)); // true
console.log(isPalindrome(testString2)); // false



// Using Two Pointers
function isPalindrome(str) {
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
}

// Helper function to check if a character is alphanumeric
function isAlphanumeric(char) {
  return /^[A-Za-z0-9]$/.test(char);
}

// Example usage
const testStr1 = "A man, a plan, a canal, Panama";
const testStr2 = "race a car";
const testStr3 = "No 'x' in Nixon";

console.log(isPalindrome(testStr1)); // true
console.log(isPalindrome(testStr2)); // false
console.log(isPalindrome(testStr3)); // true
