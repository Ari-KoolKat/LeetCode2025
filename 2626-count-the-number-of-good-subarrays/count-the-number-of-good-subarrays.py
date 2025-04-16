class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        left = 0
        good_subarrays = 0
        total_pairs = 0

        for right_value in nums:
            if right_value in freq:
                total_pairs += freq[right_value]
                freq[right_value] += 1
            else:
                freq[right_value] = 1

            while total_pairs >= k:
                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]]
                left += 1

            good_subarrays += left

        return good_subarrays