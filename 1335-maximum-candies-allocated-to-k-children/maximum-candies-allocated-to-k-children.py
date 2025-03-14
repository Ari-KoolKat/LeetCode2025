class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        l = len(candies)
        right = max(candies)
        left = 1
        if sum(candies) < k:
            return 0
        def check(max_candies):
            num_child = 0
            for elem in candies:
                num_child += (elem // max_candies)
            return num_child >= k
        ans = 0
        while(left <= right):
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans