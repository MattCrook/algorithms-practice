#------------------------------------------------------------------#
# Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#-----------------------------------------------------------------#


#---------------------------------#
# Solution 1
# Using Hashmap

# Approach
#  - Create a HashMap called dictionary to store the character counts in the magazine.
#  - Iterate through each character in the magazine string.
#  - If the character is not present in the dictionary, add it with a count of 1.
#  - If the character is already present, increment its count by 1.
#  - Iterate through each character in the ransom note string.
#  - Check if the character is present in the dictionary and its count is greater than 0.
#  - If both conditions are satisfied, decrement the count of the character in the dictionary.
#  - If a character is not present in the dictionary or its count is 0, return false.
#  - If all characters in the ransom note have been checked successfully, return true.

# Complexity
#  - Time complexity:
#    - The time complexity of the solution is O(m+n), where m is the length of the magazine string and n is the length of the ransom note string. This is because we iterate through each character in both strings once.
#  - Space complexity:
#    - The space complexity is O(m), where m is the number of unique characters in the magazine string. This is because we store the character counts in the dictionary HashMap.
#---------------------------------#
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Create a dictionary to store character counts
        dictionary = {}

        # Iterate through the magazine and count characters
        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        # Iterate through the ransom note and check character counts
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False

        return True

solution = Solution()
print(solution.canConstruct("a", "b"));
print(solution.canConstruct("aa", "ab"));
print(solution.canConstruct("aa", "aab"));
print("--------------------------");


#---------------------------------#
# Solution 2
# Using a Set to get unique characters in ransomNote.

# Complexity
#  - Time complexity: O(k∗(m+n)),
#   - k: the number of unique characters in ransomNote.
#   - m: the length of magazine.
#   - n: the length of ransomNote.
#  - Space complexity: O(26) → O(1)
#---------------------------------#
class Solution_2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True

solution_2 = Solution_2()
print(solution_2.canConstruct("a", "b"));
print(solution_2.canConstruct("aa", "ab"));
print(solution_2.canConstruct("aa", "aab"));
print("--------------------------");


#---------------------------------#
# Solution 3
#
# Complexity
#  - Time complexity: O(m+n)
#   - m: the length of magazine.
#   - n: the length of ransomNote.
# - Space complexity:
#   - O(26) → O(1)
#---------------------------------#
class Solution_3(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_hash = {}

        for c in magazine:
            magazine_hash[c] = 1 + magazine_hash.get(c, 0)

        for c in ransomNote:
            if c not in magazine_hash or magazine_hash[c] <= 0:
                return False
            magazine_hash[c] -= 1

        return True

solution_3 = Solution_3()
print(solution_3.canConstruct("a", "b"));
print(solution_3.canConstruct("aa", "ab"));
print(solution_3.canConstruct("aa", "aab"));
print("--------------------------");


#------------------------#
# Simple Solution
#------------------------#
class SimpleSolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in magazine:
            ransomNote = ransomNote.replace(char, '', 1)
        return ransomNote == ''

simple_solution = SimpleSolution()
print(simple_solution.canConstruct("a", "b"));
print(simple_solution.canConstruct("aa", "ab"));
print(simple_solution.canConstruct("aa", "aab"));
print("--------------------------");
