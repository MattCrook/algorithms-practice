#---------------------------------------------------------------#
# Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#---------------------------------------------------------------#

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# Starts at specified number, and stops at last number but - 1.

class Solution_1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # for i in the range length of haystack -  length of needle plus 1
        # - range returns us a sequence of numbers,
        # - length of haystack - length of needle (example 1 = 6), plus 1 (b/c range leaves off ending number)
        # - sadbutsad" = 9, sad" = 3... 9 - 3 is 7.
        # range(len(haystack) - len(needle)) = (0, 6)...+ 1 = (0,7)
        for i in range(len(haystack) - len(needle) + 1):
            # haystack is "sadbutsad"
            # i is current iteration...so letter. Ex) "s", "a", "d", etc...
            if haystack[i:i+len(needle)] == needle: # The colon is used within slicing notation to extract a portion of a sequence (e.g., a list, string, or tuple).
                # slice the haystack("sadbutsad") by i plus length of needle (3)
                # - Pick off the first three letters, as that is the length of the needle, and if equal to needle, return i.
                return i
        # did not find anything, so return -1
        return -1

solution_1 = Solution_1()
print(solution_1.strStr("sadbutsad", "sad"))
print(solution_1.strStr("leetcode", "leeto"))
print("--------------------------")




class Solution_2(object):
    def strStr(self, haystack, needle):
        length_needle=len(needle)
        for i in range(len(haystack)):
            test=haystack[i:length_needle+i]
            if test==needle:
                return i
        return -1

solution_2 = Solution_2()
print(solution_2.strStr("sadbutsad", "sad"))
print(solution_2.strStr("leetcode", "leeto"))
print("--------------------------")



class Solution_3:
    def strStr(self, haystack, needle):
        a, b = len(haystack), len(needle)

        for i in range(a - b + 1):
            if haystack[i:i + b] == needle:
                return i

        return -1

solution_3 = Solution_3()
print(solution_3.strStr("sadbutsad", "sad"))
print(solution_3.strStr("leetcode", "leeto"))
print("--------------------------")
