################################# INTEGER TO ROMAN ###################################
# Seven different symbols represent Roman numerals with the following values:
#
# Symbol	Value
#  I	      1
#  V	      5
#  X	      10
#  L	      50
#  C	      100
#  D	      500
#  M	      1000
#
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
# Converting a decimal place value into a Roman numeral has the following rules:
# - If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# - If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# - Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
#
# CHALLENGE:
# - Given an integer, convert it to a Roman numeral.
'''
Example 1:

Input: num = 3749
Output: "MMMDCCXLIX"
Explanation:
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

Example 2:

Input: num = 58
Output: "LVIII"
Explanation:
50 = L
 8 = VIII

Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation:
1000 = M
 900 = CM
  90 = XC
   4 = IV
'''
######################################################################################


# ------------------- SOLUTION 01 ------------------------#
# --------------------------------------------------------#
# Create "static" lists to hold the roman numerals, and the values they represent.
# - Numbers at indexes of "value" correlate to roman numerals at indexes in "roman".
# NOTE - using ALL roman numerals, despite challenge only giving example for 7....
value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Initializing empty variable that will be the final result/ value we return.
        ans = ""
        # Loop over the roman numerals list.
        # - This could theoretically be just "for i in range(13):" - as the roman numerals are static (always 13). Not expecting there to be more or less.
        # - But, added a more "dynamic" way just to practice.
        # Using range to iterate over (and returns) a sequence of numbers, starting from 0 by default, and increments by 1 (by default).
        for i in range(len(roman)):
          # Using a while loop - comparing number passed into function, to value at the current index of "value" array.
          #  - We are already in a loop:
          #   - For each index of roman,
          #   - compare the number passed in to the number at the same index in value.
          #   - Note - numbers at indexes of "value" correlate to roman numerals at indexes in "roman".
          while num >= value[i]:
            # Set answer to value at index of roman. Shorthand for: (ans = ans + roman[i])
            # - Remember - "ans" holds the roman numerals, so as long as we are in this loop, adding to our roman numerals until final answer.
            ans += roman[i]
            # Set num to current num minus the value at current index of value. (num = num - value[i])
            # - Essentially subtracting the value from the num each iteration, until we get to one or zero out.
            #  - in which our loop exits and we have our final answer.
            num -= value[i]
        return ans


solution = Solution()
print("Sol 1: ", solution.intToRoman(3749))
print("Sol 2: ", solution.intToRoman(58))
print("Sol 3: ", solution.intToRoman(1994))
print("--------------")



#------------------------ SOLUTION #2---------------------------------#
def intToRoman2(num: int) -> str:
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res = ""
    for i in d:
        res += (num//i) * d[i]
        num %= i
    return res

print("Sol 1: ", intToRoman2(3749))
print("Sol 2: ", intToRoman2(58))
print("Sol 3: ", intToRoman2(1994))
print("--------------")


#---------------------------- SOLUTION #3 -----------------------------#
def intToRoman3(num: int):
    roman = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
      }
    romanized = ''
    for base, symb in roman.items():
        romanized += symb * (num // base)
        num %= base
    else:
        return romanized

print("Sol 1: ", intToRoman3(3749))
print("Sol 2: ", intToRoman3(58))
print("Sol 3: ", intToRoman3(1994))
print("--------------")


#----------------------------- SOLUTION #4 ----------------------------#
# No need to create big table 
#---------------------------------------------------------#
def intToRoman4(num: int) -> str:
	ones = ['I', 'X', 'C', 'M']
	fives = ['V', 'L', 'D']
	i = 0
	ans = []

	while num > 0:
		n = num % 10
		if 1 <= n <= 3:
			ans.append(ones[i] * n) 
		elif n == 4:
			ans.append(ones[i] + fives[i])
		elif 5 <= n <= 8:
			ans.append(fives[i] + ones[i] * (n - 5))
		elif n == 9:
			ans.append(ones[i] + ones[i+1])

		i += 1
		num //= 10

	return "".join(ans[::-1])

print("Sol 1: ", intToRoman4(3749))
print("Sol 2: ", intToRoman4(58))
print("Sol 3: ", intToRoman4(1994))
print("--------------")
