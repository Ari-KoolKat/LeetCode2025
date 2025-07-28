class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num

        count = 0 
        for mask in range(1, 1 << n):
            current = 0
            for i in range (n):
                if mask & (1 << i):
                    current |= nums[i]
            if current == max_or:
                count += 1

        return count