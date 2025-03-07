class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Step 1: Sieve of Eratosthenes
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False

        # Step 2: Collect primes in the given range
        primes = [i for i in range(left, right + 1) if sieve[i]]

        # Step 3: Find the closest prime pair
        if len(primes) < 2:
            return [-1, -1]

        min_gap = float('inf')
        result = [-1, -1]

        for i in range(1, len(primes)):
            gap = primes[i] - primes[i - 1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i - 1], primes[i]]

        return result