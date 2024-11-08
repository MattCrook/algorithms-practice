#---------------------------------------------------------------#
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#---------------------------------------------------------------#

class Solution_01(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n

        prv1 = 1
        prv2 = 2
        x = 0
        for i in range(2,n):
            x = prv1 + prv2
            prv1 = prv2
            prv2 = x
        return x

solution_01 = Solution_01()
print("solution_01: ", solution_01.climbStairs(2))
print("solution_01: ", solution_01.climbStairs(3))
print("--------------------------")




class Solution_2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n):
             if n==1: #only one step option is availble
                 return 1
             if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
                 return 2
             return climb(n-1) + climb(n-2)
        return climb(n)

solution_02 = Solution_2()
print("solution_02: ", solution_02.climbStairs(2))
print("solution_02: ", solution_02.climbStairs(3))
print("--------------------------")


# Recursion
class Solution_3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo ={}
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo: # if the recurssion already done before first take a look-up in the look-up table
                return memo[n]
            else:   # Store the recurssion function in the look-up table and reuturn the stored look-up table function
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]

        return climb(n)

solution_03 = Solution_3()
print("solution_03: ", solution_03.climbStairs(2))
print("solution_03: ", solution_03.climbStairs(3))
print("--------------------------")


# Idea 3 : Dynamic programming
# --> store the distinct ways in a dynamic table
def climb(n):
    #edge cases
    if n==0: return 0
    if n==1: return 1
    if n==2: return 2
    dp = [0]*(n+1) # considering zero steps we need n+1 places
    dp[1]= 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] +dp[i-2]
    #print(dp)
    return dp[n]

print("solution_04: ", climb(2))
print("solution_04: ", climb(3))
print("--------------------------")



# Backtracking with DP Memoization
class Solution_5(object):
    def climbStairs(self, n):
        cache = {}
        def backtracking(total):
            if total == n:
                return 1
            if total > n:
                return 0
            if total in cache:
                return cache[total]
            cache[total] = backtracking(total + 1) + backtracking(total + 2)
            return cache[total]
        return backtracking(0)

solution_05 = Solution_5()
print("solution_05: ", solution_05.climbStairs(2))
print("solution_05: ", solution_05.climbStairs(3))
print("--------------------------")
