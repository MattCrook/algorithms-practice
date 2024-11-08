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
