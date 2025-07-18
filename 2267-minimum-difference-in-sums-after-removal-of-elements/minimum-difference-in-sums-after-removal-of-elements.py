class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq

class Solution:
    def minimumDifference(self, nums):
        N = len(nums)
        n = N // 3

        left_min_sum = [0] * N
        right_max_sum = [0] * N

        max_heap = []
        left_sum = 0

        for i in range(2 * n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i]

            if len(max_heap) > n:
                left_sum += heapq.heappop(max_heap) 
            if len(max_heap) == n:
                left_min_sum[i] = left_sum

        min_heap = []
        right_sum = 0

        for i in range(N - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i]

            if len(min_heap) > n:
                right_sum -= heapq.heappop(min_heap)
            if len(min_heap) == n:
                right_max_sum[i] = right_sum

        result = float('inf')

        for i in range(n - 1, 2 * n):
            result = min(result, left_min_sum[i] - right_max_sum[i + 1])

        return result