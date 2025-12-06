class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp_sum = [0] * (n + 2)
        dp_sum[1] = 1
        
        max_d = deque()
        min_d = deque()
        
        left = 0
        
        for i in range(n):
            while max_d and nums[max_d[-1]] <= nums[i]:
                max_d.pop()
            max_d.append(i)
            
            while min_d and nums[min_d[-1]] >= nums[i]:
                min_d.pop()
            min_d.append(i)
            
            while nums[max_d[0]] - nums[min_d[0]] > k:
                left += 1
                if max_d[0] < left:
                    max_d.popleft()
                if min_d[0] < left:
                    min_d.popleft()
            
            current_ways = (dp_sum[i+1] - dp_sum[left]) % MOD
            dp[i+1] = current_ways
            dp_sum[i+2] = (dp_sum[i+1] + current_ways) % MOD
        
        return dp[n]