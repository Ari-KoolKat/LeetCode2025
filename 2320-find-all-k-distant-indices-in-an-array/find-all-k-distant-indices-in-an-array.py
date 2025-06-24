class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result_set = set()

        for j in range(n):
            if nums[j] == key:
                start = max(0, j - k)
                end = min(n - 1, j + k)
                for i in range(start, end + 1):
                    result_set.add(i)

        return sorted(result_set)