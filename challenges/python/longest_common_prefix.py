#-----------------------------------------------------------------------#
# Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#-----------------------------------------------------------------------#
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
for word in strs1:
  letters1 = list(word)
  letters2 = [l for l in word]
  print("letters1: ", letters1)
  print("letters2: ", letters2)
print("--------------------------------")



#------ Fairly Simple Solution ------#
class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
          # range(0, 6)
          # range(0, 3)
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base

solution = Solution()
print("solution", solution.longestCommonPrefix(strs1))
print("solution", solution.longestCommonPrefix(strs2))
print("--------------------------------")


#---- Very similar to above solution, but making better with using while loop ----#
class SolutionRefactor(object):
    def longestCommonPrefix(self, strs):
        # To improve execution time, always remove special use cases at the beginning.
        if len(strs) == 0:
          return ""
        # initialize variable, set to first index of str ("flower" or "dog")
        prefix = strs[0]
        # slicing the list, starting on index 1. (b/c we have index 0 from prefix)
        # - so strs[1:] is ['flow', 'flight'], or ['racecar', 'car']
        # and iterating the strings/ words...
        for string in strs[1:]:
          # The startswith() method returns True if the string starts with the specified value, otherwise False.
          #   - string.startswith(value, start, end)
          # So, prefix == "fl"
          # So...While string.startswith(prefix) is False, meaning we are not finding a match,
          # Keep iterating....
          while not string.startswith(prefix):
            # And for each iteration, slice the string (current iterator),
            # with ending slice 1 less the last index, to keep narrowing down word.
            #    - Slice: sequence[start:end:step]
            # Example:
            #   - flowe
            #   - flow
            #   - flo
            #   - fl
            # Loop stops when finds matching prefix.
            # note this is also mutating the variable we set.
            prefix = prefix[:-1]
            # Take care of clean up, and per directions, return an empty string if loop finds nothing.
            if not prefix:
              return ""
            # otherwise return the prefix.
        return prefix

solution_refactor = SolutionRefactor()
print("solution_refactor", solution_refactor.longestCommonPrefix(strs1))
print("solution_refactor", solution_refactor.longestCommonPrefix(strs2))
print("--------------------------------")


#-----------#
# To find the longest common prefix among an array of strings, we can compare the characters of all strings from left to right until we encounter a mismatch. 
# The common prefix will be the characters that are the same for all strings until the first mismatch.
#
# Approach
# - If the input array strs is empty, return an empty string because there is no common prefix.
# - Initialize a variable prefix with an initial value equal to the first string in the array strs[0].
# - Iterate through the rest of the strings in the array strs starting from the second string (index 1).
# - For each string in the array, compare its characters with the characters of the prefix string.
# - While comparing, if we find a mismatch between the characters or if the prefix becomes empty, return the current value of prefix as the longest common prefix.
# - After iterating through all strings, return the final value of prefix as the longest common prefix.
#-----------#
class SolutionRefactor2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

solution_refactor2 = SolutionRefactor2()
print("solution_refactor2", solution_refactor2.longestCommonPrefix(strs1))
print("solution_refactor2", solution_refactor2.longestCommonPrefix(strs2))
print("--------------------------------")


#----------- Longer more complex Solution -------------#
class Solution3(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1 : # To improve execution time, always remove special use cases at the beginning.
            return strs[0]
        pref_res = ""

        # Compare just two first elms, and get the longest prefix, after that continue looping over rest of elms and remove prefixs
        for i in range(0, min(len(strs[0]), len(strs[1]))):
            if strs[0][i] != strs[1][i] :
                break

            pref_res += strs[0][i]

        # Now we have something to start with, we'll continue to check on rest array and remove  any char that doesn't match  :
        for rest_char in strs[2:]:
            while pref_res != rest_char[:len(pref_res)] : # Removing not matching chars
                pref_res = pref_res[:-1]


        return pref_res

solution_3 = Solution3()
print("solution_3", solution_3.longestCommonPrefix(strs1))
print("solution_3", solution_3.longestCommonPrefix(strs2))
print("--------------------------------")


class FindLongestCommonPrefix(object):
  def findLongestCommonPrefix(self, strings):
      #common_prefix = []
      if len(strings) == 0:
          return ""
      prefix = strings[0]
      for word in strings[1:]:
          while not word.startswith(prefix):
              prefix = prefix[:-1]
          if not prefix:
              return ""
      #common_prefix.append(prefix)
      #return common_prefix
      return prefix

  def returnList(self, strings):
      common_prefix = []
      longestCommonPrefix = self.findLongestCommonPrefix(strings)
      common_prefix.append(longestCommonPrefix)
      return common_prefix


findLongestCommonPrefix = FindLongestCommonPrefix()
print("Return List", findLongestCommonPrefix.returnList(strs1))
print("--------------------------------")
