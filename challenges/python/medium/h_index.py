#############################################################
# H INDEX
#
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# - According to the definition of h-index on Wikipedia:
#   - The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
#
# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1
#############################################################

citations_01 = [3,0,6,1,5]
citations_02 = [1,3,1]

#------------ SOLUTION #1 ----------------#
# The h-index is a metric to evaluate the impact of a researcher's publications. It is defined as the maximum value h such that the researcher has published at least h papers that have each been cited at least h times.
#  - The problem can be solved by sorting the array and iterating through it to check where the condition is satisfied.
# Key idea: After sorting the array, the number of papers with citations greater than or equal to a certain value can be easily determined using their index.

# Approach
#  - Sort the citations array:
#  - This organizes the citation counts in ascending order, making it easier to check the number of papers with citations ≥ h.

# Iterate through the sorted array:
#  - For each citation at index i, calculate the number of papers with citations greater than or equal to the current value. 
#  - This is given by citations.size() - i (in C++ terms) or citations.length - i (in other languages).

# Check two cases:
#  - If the citation count at the current index (citations[i]) is less than or equal to the number of papers (citations.length - i), update h_ind as the maximum of its current value and the citation count.
#  - Otherwise, calculate the h-index using the number of remaining papers (citations.length - i).

# Return the maximum h_ind value:
# - This value represents the highest h-index that satisfies the condition for the given array of citations.

# Complexity
#  - Time complexity: O(nlog n)
#  - Space complexity: O(1)
#-----------------------------------------#
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        h_ind = 0
        for i in range(len(citations)):
            if citations[i] <= len(citations) - i:
                h_ind = max(h_ind, citations[i])
            else:
                l = len(citations) - i
                h_ind = max(h_ind, l)
        return h_ind

solution_01 = Solution()
print("citations_01", solution_01.hIndex(citations_01))
print("citations_02", solution_01.hIndex(citations_02))
print("----------------------------")


#------------ SOLUTION #2 ----------------#
# - One-liner
# ----------------------------------------#
class Solution_02(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))

solution_02 = Solution_02()
print("citations_01", solution_02.hIndex(citations_01))
print("citations_02", solution_02.hIndex(citations_02))
print("----------------------------")
