#---------------------------------------------------------------#
# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#---------------------------------------------------------------#


# Normalization: ''.join(c.lower() for c in s if c.isalnum()) converts the string to lowercase and removes any non-alphanumeric characters (using isalpha() or isdigit()).
# Palindrome check: normalized_s == normalized_s[::-1] checks if the string is equal to its reverse.
class Solution():
     def isPalindrome(self, s: str) -> bool:
         # Normalize the string: convert to lowercase and keep only alphanumeric characters
         normalized_s = ''.join(c.lower() for c in s if c.isalnum())

         # Check if the normalized string is the same forwards and backwards
         return normalized_s == normalized_s[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))
print("--------------------------")


class Solution_1(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

solution_1 = Solution_1()
print(solution_1.isPalindrome("A man, a plan, a canal: Panama"))
print(solution_1.isPalindrome("race a car"))
print(solution_1.isPalindrome(" "))
print("--------------------------")

# Solution using operator ~
# ~: Bitwise NOT
class Solution_2:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))

solution_2 = Solution_2()
print(solution_2.isPalindrome("A man, a plan, a canal: Panama"))
print(solution_2.isPalindrome("race a car"))
print(solution_2.isPalindrome(" "))
print("--------------------------")


# Solution using two pointers:
class Solution_3:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True

solution_3 = Solution_3()
print(solution_3.isPalindrome("A man, a plan, a canal: Panama"))
print(solution_3.isPalindrome("race a car"))
print(solution_3.isPalindrome(" "))
print("--------------------------")

# Using two pointers:
class Solution_4:
	def isPalindrome(self, s: str) -> bool:
		string = ''
		for n in s:
			if n.isalnum():
				string += n.lower()

		l, r = 0, len(string) - 1

		while l < r:
			if string[l] == string[r]:
				l += 1
				r -= 1
			else:
				return False

		return True

solution_4 = Solution_4()
print(solution_4.isPalindrome("A man, a plan, a canal: Panama"))
print(solution_4.isPalindrome("race a car"))
print(solution_4.isPalindrome(" "))
print("--------------------------")



# How do you define a palindrome
# Dees it need to be a real word
# Do the letters need to be a substring, or a sequence
# Is there a limit to the length of the string < input
def findPalindrome(string):
    results = []
    # Base case, if the string is one letter, then it qualifies as a palindrome
    if len(string) == 1:
        results.append(string)
        return results
    # this will solve for the single character case.
    # But it will not solve for palindromes with length greater than 1.
    # we need to check that the left most and right most characters are equal.
    # IF so, we can add all the palindromes that qualify within the string.

    right = string[len(string) - 1].lower()
    left = string[0].lower()
    # check for all the palindromes where the string does not have the right most character,
    # and then check for where all the palindromes where the string does not have the left most letter.
    results.append(findPalindrome(right))
    results.append(findPalindrome(left))

    if right == left:
        # turn all to lower case, loop through letters and check if it is alphanumeric..and concatenate the list of strings.
        alpha_numeric_chars = ''.join(character.lower() for character in string if character.isalnum())
        results.append(alpha_numeric_chars)


    return results


print(findPalindrome("A man, a plan, a canal: Panama"))


#--------------------#
# Using Recursion (and Memoization)
#
#  Expect the calculations to have to perform repeat operations. (like finding "aba" multiple times,)
# -Memoization can be a good solution to fetch results that have already been calculated.
#
# Abstracted out helper functions:
# Helper function (preprocessHelper) to process the string by filtering out non-alphanumeric characters.
# Recursive helper function (check) to check palindrome

# Preprocessing:
# - The preprocessHelper function filters out non-alphanumeric characters and converts the string to lowercase.
# Recursive Check:
# - The checkHelper function compares the first and last characters (s[left] and s[right]).
# - If they are equal, it calls itself recursively on the substring excluding the first and last characters (left + 1, right - 1).
# - The recursion continues until the left pointer meets or exceeds the right pointer, at which point the string is confirmed to be a palindrome.

# Time Complexity:
# - The preprocessing step has a time complexity of O(n), where n is the length of the string.
# - The recursion checks each character once, so the recursive check also has a time complexity of O(n).
# - Thus, the overall time complexity of this solution is O(n), where n is the length of the string.
# Space Complexity:
#  - The space complexity is O(n) due to the string created during preprocessing and the recursive stack.
#--------------------#

class SolutionUsingRecursion(object):
    def findPalindrome(self, input_string: str) -> bool:

        # turn all to lower case, loop through letters (of input_string) and check if it is alphanumeric...and concatenate the list of strings, by ''.join()
        def preprocessHelper(string: str) -> str:
            alpha_numeric_chars = ''.join(character.lower() for character in string if character.isalnum())
            return alpha_numeric_chars

        def checkHelper(input_string, left, right):
            # Base case: when left index is greater than or equal to right, (assume) it's a palindrome.
            # - left and right are induces in string passed in.
            # Exit and return as left pointer meets or exceeds the right pointer
            if left >= right:
                return True
            # Compare characters at left and right positions
            if input_string[left] != input_string[right]:
                return False
            # Recurse with the next positions, (from the left one more to the right, and from the right one more to the left)
            return checkHelper(input_string, left + 1, right - 1)

        # Preprocess the string to remove non-alphanumeric characters and make it lowercase
        processed_string = preprocessHelper(input_string)

        # Start the recursion with the full string
        return checkHelper(processed_string, 0, len(processed_string) - 1)

solution_using_recursion = SolutionUsingRecursion()
print(solution_using_recursion.findPalindrome("A man, a plan, a canal: Panama"))
print(solution_using_recursion.findPalindrome("race a car"))
print(solution_using_recursion.findPalindrome(" "))
print("--------------------------")
