#---------------------------------------------------------------#
# Reverse bits of a given 32 bits unsigned integer.
# Note:
#  Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#  In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
#---------------------------------------------------------------#

# Approach:
#  - We can reverse bits of a given number by iterating over all bits of the given number and adding the bits in the reverse order. 
#  - To reverse the bits, we can use a variable and left shift it by 1 in each iteration. 
#  - We can then add the last bit of the given number to the reversed number by performing an AND operation with the last bit of the given number. 
#  - Once we add the last bit of the given number, we can right shift the given number by 1 to remove the last bit.
# Algorithm:
#  - Initialize the reversed number to 0.
#  - Iterate over all 32 bits of the given number.
#  - In each iteration, left shift the reversed number by 1 and add the last bit of the given number to it.
#  - To add the last bit of the given number to the reversed number, perform an AND operation with the given number and 1.
#  - Right shift the given number by 1 to remove the last bit.
#  - Repeat steps 3-5 for all 32 bits of the given number.
#  - Return the reversed number.
class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the reversed number to 0
        reversed_num = 0

        # Iterate over all 32 bits of the given number
        for i in range(32):
            # Left shift the reversed number by 1 and add the last bit of the given number to it
            reversed_num = (reversed_num << 1) | (n & 1)
            # To add the last bit of the given number to the reversed number, perform an AND operation with the given number and 1
            n >>= 1

        # Return the reversed number
        return reversed_num

solution = Solution()
print(solution.reverseBits(0o000010100101000001111010011100))
print(solution.reverseBits(11111111111111111111111111111101))
print("--------------------------")


class Solution_01:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

solution_01 = Solution_01()
print(solution_01.reverseBits(0o000010100101000001111010011100))
print(solution_01.reverseBits(11111111111111111111111111111101))
print("--------------------------")


class Solution_2:
  def reverseBits(self, n):
      # 32bin to string
      x= format(n, '032b')

      # reverse the string then convert it to int
      y= int(x[::-1],2)

      return y

solution_2 = Solution_2()
print(solution_2.reverseBits(0o000010100101000001111010011100))
print(solution_2.reverseBits(11111111111111111111111111111101))
print("--------------------------")


class Solution_3:
    def reverseBits(self, n: int) -> int:
        n = format(n, 'b')
        n = n.zfill(32)

        return int(n[::-1], 2)

    def reverseBitsOneLne(self, n: int) -> int:
        return int(format(n, 'b').zfill(32)[::-1], 2)


solution_3 = Solution_3()
print(solution_3.reverseBits(0o000010100101000001111010011100))
print(solution_3.reverseBits(11111111111111111111111111111101))
print(solution_3.reverseBitsOneLne(0o000010100101000001111010011100))
print(solution_3.reverseBitsOneLne(11111111111111111111111111111101))
print("--------------------------")
