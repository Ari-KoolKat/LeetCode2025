class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        half_k = k // 2
        
        current_total_profit = 0
        original_contribution = []
        
        for p, s in zip(prices, strategy):
            val = p * s
            current_total_profit += val
            original_contribution.append(val)
            
        current_window_original_sum = sum(original_contribution[:k])
        current_second_half_price_sum = sum(prices[half_k:k])
        
        max_gain = current_second_half_price_sum - current_window_original_sum
        
        for i in range(1, n - k + 1):
            prev_start = i - 1
            new_end = i + k - 1
            
            current_window_original_sum -= original_contribution[prev_start]
            current_window_original_sum += original_contribution[new_end]
            
            element_leaving_second_half = prices[i - 1 + half_k]
            element_entering_second_half = prices[new_end]
            
            current_second_half_price_sum -= element_leaving_second_half
            current_second_half_price_sum += element_entering_second_half
            
            current_gain = current_second_half_price_sum - current_window_original_sum
            if current_gain > max_gain:
                max_gain = current_gain
                
        return current_total_profit + max(0, max_gain)