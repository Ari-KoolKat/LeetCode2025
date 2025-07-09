class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]           
                    
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]  
        gaps[n] = eventTime - endTime[-1]            
        
        max_sum = 0
        curr_sum = 0
        left = 0
        
        for right in range(n + 1):
            curr_sum += gaps[right]
            
            while right - left + 1 > k + 1:
                curr_sum -= gaps[left]
                left += 1
            
            max_sum = max(max_sum, curr_sum)
        
        return max_sum