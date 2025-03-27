class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        total_count = nums.count(candidate)

        prefix_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                prefix_count += 1

            left_valid = 2 * prefix_count > (i + 1)
            right_valid = 2 * (total_count - prefix_count) > (len(nums) - i - 1)

            if left_valid and right_valid:
                return i
        
        return -1