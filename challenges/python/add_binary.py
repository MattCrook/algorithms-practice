#---------------------------------------------------------------#
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#---------------------------------------------------------------#

# One Liner
class Solution_1(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


solution_1 = Solution_1()
print("Example 1: ", solution_1.addBinary("11", "1"))
print("Example 2: ", solution_1.addBinary("11", "1"))
print("--------------------------")



# To solve the problem of adding two binary strings, we can simulate the process of binary addition.
class Solution_2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            result.append(str(carry % 2))
            carry //= 2
        return ''.join(result[::-1])


solution_2 = Solution_2()
print("Example 1: ", solution_2.addBinary("11", "1"))
print("Example 2: ", solution_2.addBinary("11", "1"))
print("--------------------------")
