class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_unique = len(set(nums))
        freq = defaultdict(int)
        left = 0
        count = 0
        n = len(nums)

        for right in range(n):
            freq[nums[right]] += 1

            while len(freq) == total_unique:
                count += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count