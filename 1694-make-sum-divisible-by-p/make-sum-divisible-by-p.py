class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = 0
        for num in nums:
            total = (total + num) % p

        k = total % p
        if k == 0:
            return 0

        return self.minimumSubArraySumEqualsK(nums, k, p)

    def minimumSubArraySumEqualsK(self, nums, k, p):
        n = len(nums)
        mp = {0: -1}  # prefix_mod -> index
        prefix = 0
        min_len = float('inf')

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            remain = (prefix - k + p) % p

            if remain in mp:
                min_len = min(min_len, i - mp[remain])

            mp[prefix] = i

        if min_len == n:
            return -1
        return -1 if min_len == float('inf') else min_len