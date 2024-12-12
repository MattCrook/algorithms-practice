##############################################################
# (Arrays And Strings)
# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
##############################################################

#-----------------------------------------#
# SOLUTION 1
# Approach
# - Initialize variables buy with the first element of the prices array and profit as 0.
# - Iterate through the prices starting from the second element.
# - Update the buy variable if the current price is lower than the current buying price.
# - Update the profit if the difference between the current price and the buying price is greater than the current profit.
# - Return the final profit.

# Kadane's Algorithm:
# - Kadane's Algorithm is a dynamic programming technique used to find the maximum subarray sum in an array of numbers. 
# - The algorithm maintains two variables: 
#     - max_current represents the maximum sum ending at the current position, 
#     - max_global represents the maximum subarray sum encountered so far. 
# - At each iteration, it updates max_current to include the current element or start a new subarray if the current element is larger than the accumulated sum. 
# - The max_global is updated if max_current surpasses its value.

# Relating with the Approach
# - In the provided approach for finding the maximum profit in stock prices, the algorithm can be seen as a variation of Kadane's Algorithm. Instead of finding the maximum subarray sum directly, it focuses on finding the maximum positive difference between consecutive elements (prices) in the array.

# Initialization:
# - In Kadane's Algorithm, max_current and max_global are initialized to the first element of the array.
# - In the stock profit approach, buy is initialized with the first element of the prices array, and profit is initialized to 0.
# Iteration:
# - Kadane's Algorithm iterates through the array, updating max_current based on the current element's value and deciding whether to start a new subarray.
# - The stock profit approach iterates through the prices array, updating buy when a lower price is encountered and treating the difference between the current price and buy as a potential profit.
# Comparison and Update:
# - Kadane's Algorithm compares and updates max_current and max_global at each iteration.
# - The stock profit approach compares and updates profit whenever a positive difference between the current price and buy exceeds the current profit.

# Complexity
# - Time complexity: O(n), where n is the length of the prices array. The algorithm iterates through the array once.
# - Space complexity: O(1), as only a constant amount of extra space is used.

# Math Step through
# ---
# buy = 7
# profit = 0
# prices[i] = 1
# ---
# if 1 < 7
# buy = 1
# --
# prices[i] = 5
# if 5 - 1 > 0
# profit = 4
# ---
# prices[i] = 3
# 3  not less than 1
# 3 - 1 not less than 4
# ---
# prices[i] = 6
# 6 -1 > 4
# profit = 6 - 1 = 5
# ---
#-----------------------------------------#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0] # initializing var with first index if list.
        profit = 0
        for i in range(1, len(prices)): # Iterate through the prices starting from the second element.
            # current_price = prices[i] # saving off value (for better readability)
            if prices[i] < buy:
                buy = prices[i] # Update the buy variable if the current price is lower than the current buying price.
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
print("------------------")


#------------------------------------#
# Solution 2
#------------------------------------#
class Solution2:
    def maxProfit(self, prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

solution2 = Solution2()
print(solution2.maxProfit([7,1,5,3,6,4]))
print(solution2.maxProfit([7,6,4,3,1]))
print("------------------")


#------------------------------------#
# Solution 3 (Cleaner)
#------------------------------------#
class Solution3:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit

solution3 = Solution3()
print(solution3.maxProfit([7,1,5,3,6,4]))
print(solution3.maxProfit([7,6,4,3,1]))
print("------------------")


#------------------------------------#
# Solution 4
# A brute force approach would calculate every possible buy-sell combination and would run in O(n^2), but we can reduce this to O(n) by avoiding unncessary computations. The strategy below iterates once for every sell date, and handles two cases:
# - If buy price < sell price, calculate the profit and compare it to the max profit so far. If it is greater than the max profit, replace it. Also, there is no need to go back and calculate profits using this sell date as a buy date, since we can always achieve a higher profit from using the original buy date (which is at a lower price).
# - If sell price <= buy date, simply update the buy date to be the current sell date, since we have found a lower price to buy from.
# - At the end, return profit, which will contain the maximum profit achievable
#------------------------------------#
class Solution4(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for sell in prices[1:]: # splitting list (starting at index 1 rather than 0 - bc we have index zero (buy))
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit

solution4 = Solution4()
print(solution4.maxProfit([7,1,5,3,6,4]))
print(solution4.maxProfit([7,6,4,3,1]))
print("------------------")
