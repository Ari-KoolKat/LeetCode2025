class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Start with one even prefix sum (the sum of zero elements)
        current_sum = 0
        odd_subarray_count = 0

        for num in arr:
            current_sum += num

            # Check if the current prefix sum is odd or even
            if current_sum % 2 == 0:
                # Current sum is even
                odd_subarray_count = (odd_subarray_count + odd_count) % MOD
                even_count += 1  # Increment the count of even prefix sums
            else:
                # Current sum is odd
                odd_subarray_count = (odd_subarray_count + even_count) % MOD
                odd_count += 1  # Increment the count of odd prefix sums

        return odd_subarray_count