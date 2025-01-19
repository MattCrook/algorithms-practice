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

# citations_01 = [3,0,6,1,5]
# citations_02 = [1,3,1]
#############################################################


#------------ SOLUTION #1 ----------------#
# The h-index is a metric to evaluate the impact of a researcher's publications.
# It is defined as the maximum value h such that the researcher has published at least h papers that have each been cited at least h times.
#  - The problem can be solved by sorting the array and iterating through it to check where the condition is satisfied.
# Key idea: After sorting the array, the number of papers with citations greater than or equal to a certain value can be easily determined using their index.
#
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
        # Sort the citations array:
        # This organizes the citation counts in ascending order, making it easier to check the number of papers with citations ≥ h.
        citations.sort()
        # initialize and set an initial value for h index to 0.
        h_ind = 0
        # Iterate through the sorted array:
        #  - For each citation at index i, calculate the number of papers with citations greater than or equal to the current value.
        #  - This is given by citations.size() - i (in C++ terms) or citations.length - i (in other languages).
        #    - Use range(len()) here to iterate the index's: i => [0,1,2,3,4]
        #      - Otherwise iterating just citations: for i in citations => [0,1,3,5,6]
        for i in range(len(citations)):
            # Check two cases:
            #  - If the citation count at the current index (citations[i]) is less than or equal to the number of papers (citations.length - i), update h_ind as the maximum of its current value and the citation count.
            #  - Otherwise, calculate the h-index using the number of remaining papers (citations.length - i).
            if citations[i] <= len(citations) - i:
                h_ind = max(h_ind, citations[i])
            else:
                l = len(citations) - i
                h_ind = max(h_ind, l)
        # Return the maximum h_ind value:
        # - This value represents the highest h-index that satisfies the condition for the given array of citations.
        return h_ind

solution_01 = Solution()
print("citations_01", solution_01.hIndex([3,0,6,1,5]))
print("citations_02", solution_01.hIndex([1,3,1]))
print("----------------------------")


#------------ SOLUTION #2 ----------------#
# One-liner
# - May not be the bet solution in an interview but can do it in one line.
# ----------------------------------------#
class Solution_02(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))

solution_02 = Solution_02()
print("citations_01", solution_02.hIndex([3,0,6,1,5]))
print("citations_02", solution_02.hIndex([1,3,1]))
print("----------------------------")



#------------ SOLUTION #3----------------#
# To compute the researcher's h-index, we can sort the citations array in non-increasing order and then iterate through the sorted array.
# - For each citation count, we compare it to the number of papers that have at least that many citations, which can be calculated as the remaining elements in the array.
# - If the citation count is greater than or equal to the number of papers with at least that many citations, we have found the h-index.

# For example, given the citations array [3,0,6,1,5], we can sort it to obtain [6,5,3,1,0].
# - We then iterate through the sorted array and for each citation count, we compare it to the number of remaining elements in the array.
# - For the first element, 6, there are 5 remaining elements in the array, all of which have at least 6 citations, so the h-index is 6.
# - For the second element, 5, there are 4 remaining elements in the array, all of which have at least 5 citations, so the h-index is 5.
# - For the third element, 3, there are 3 remaining elements in the array that have at least 3 citations, so the h-index is 3.

# Time Complexity:
#  - O(nlogn), where n is the length of the citations array.
#  - This is because we need to sort the array in non-increasing order, which takes O(nlogn) time.
# Space Complexity:
#  - O(1), as we are sorting the array in-place and using only constant extra space.
#----------------------------------------#
class Solution_03:
    def hIndex(self, citations):
        # Sort the array in non-increasing order
        citations.sort(reverse=True)
        n = len(citations)
        h = 0
        # Iterate through the sorted array and compare each citation count to the number of papers that have at least that many citations
        for i in range(n):
            # If the citation count is greater than or equal to the number of papers with at least that many citations, we have found the h-index
            if citations[i] >= i + 1:
                h = i + 1
        return h

solution_03 = Solution_03()
print("citations_01", solution_03.hIndex([3,0,6,1,5]))
print("citations_02", solution_03.hIndex([1,3,1]))
print("----------------------------")
