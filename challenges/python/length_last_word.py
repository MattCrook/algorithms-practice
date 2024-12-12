########################################################
# Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
########################################################

#--------------------------------#
# Solution 1
# To solve this problem, we need to find the last word in the string and return its length. We can achieve this by splitting the string into words and then returning the length of the last word.

# Approach
# 1. Strip trailing whitespaces from the input string using the strip() method.
# 2. Split the string into words using the split() method.
# 3. If there are no words after stripping whitespaces, return 0.
# 4. Otherwise, return the length of the last word, which is the last element in the list of words.

# Time complexity:
# 1. Stripping trailing whitespaces takes linear time, so it's O(n) where n is the length of the input string.
# 2. Splitting the string into words also takes linear time, so it's also O(n).
# 3. The overall time complexity is O(n).
# Space complexity:
# We store the list of words, which could take up to O(n) space if all characters in the input string are non-whitespace.
#--------------------------------#
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split()
        if not words:
          return 0
        return len(words[-1])


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))
print("--------------------")



class SolutionOneLiner(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len((s.strip()).split(" ")[-1])

solution_one_liner = SolutionOneLiner()
print(solution_one_liner.lengthOfLastWord("Hello World"))
print(solution_one_liner.lengthOfLastWord("   fly me   to   the moon  "))
print(solution_one_liner.lengthOfLastWord("luffy is still joyboy"))
print("--------------------")

class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(' ')
        for i in range(len(lst)-1,-1,-1):
            if lst[i]:
                return len(lst[i])
        return 0

solution2 = Solution2()
print(solution2.lengthOfLastWord("Hello World"))
print(solution2.lengthOfLastWord("   fly me   to   the moon  "))
print(solution2.lengthOfLastWord("luffy is still joyboy"))
print("--------------------")

# Fast Code
class Solution3(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1 
        length = 0

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length

solution3 = Solution3()
print(solution3.lengthOfLastWord("Hello World"))
print(solution3.lengthOfLastWord("   fly me   to   the moon  "))
print(solution3.lengthOfLastWord("luffy is still joyboy"))
print("--------------------")
