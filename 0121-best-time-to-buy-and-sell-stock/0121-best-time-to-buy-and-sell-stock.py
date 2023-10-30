class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_result = 0
        
        index = 0
        min_value = prices[index]
        max_value = prices[index]
        while True:
            if index > len(prices)-1:
                break
            
            if min_value > prices[index]:
                min_value = prices[index]
                max_value = prices[index]
            elif max_value < prices[index]:
                max_value = prices[index]
                max_result = max(max_result, max_value-min_value)
            index += 1
        
        return max_result