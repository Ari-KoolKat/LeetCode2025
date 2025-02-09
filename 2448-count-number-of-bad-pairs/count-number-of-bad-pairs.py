class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_pairs = n * (n - 1) // 2  # Total pairs (i, j) with i < j
        count_map = {}  # To count occurrences of k - nums[k]

        for i in range(n):
            key = i - nums[i]  # Calculate k - nums[k]
            if key in count_map:
                count_map[key] += 1
            else:
                count_map[key] = 1

        good_pairs = 0
        for count in count_map.values():
            good_pairs += count * (count - 1) // 2  # Count good pairs for this key

        bad_pairs = total_pairs - good_pairs  # Calculate bad pairs
        return bad_pairs