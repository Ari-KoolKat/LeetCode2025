class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        counts = [0] * (n + 1)
        k = 0
        total = 0

        for i in range(n):
            num = nums[i]
            while total + counts[i] < num:
                if k == len(queries):
                    return -1
                left, right, value = queries[k]
                k += 1

                if right < i:
                    continue
                counts[max(left, i)] += value
                counts[right + 1] -= value

            total += counts[i]
        return k