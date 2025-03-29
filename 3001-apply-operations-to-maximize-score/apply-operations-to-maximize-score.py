class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        MOD = 10**9 + 7
        
        def prime_factors_count(n):
            """Returns the number of distinct prime factors of n."""
            count = 0
            factors = set()
            for i in range(2, int(sqrt(n)) + 1):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 1:
                factors.add(n)
            return len(factors)

        n = len(nums)
        prime_scores = [prime_factors_count(num) for num in nums]
        
        left = [-1] * n
        right = [n] * n
        stack = []

        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        subarray_counts = []
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            subarray_counts.append((nums[i], prime_scores[i], count))

        subarray_counts.sort(reverse=True)
        
        score = 1
        for num, _, count in subarray_counts:
            take = min(k, count)
            score = (score * pow(num, take, MOD)) % MOD
            k -= take
            if k == 0:
                break
        
        return score