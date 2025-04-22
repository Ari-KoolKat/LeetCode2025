class Solution(object):
    def idealArrays(self, length, maxValue):
        """
        :type length: int
        :type maxValue: int
        :rtype: int
        """
        MOD = 10**9 + 7
        factorial, inverse, inverse_factorial = [[1] * 2 for _ in xrange(3)]

        def compute_nCr(n, r):
            while len(inverse) <= n: 
                factorial.append(factorial[-1] * len(inverse) % MOD)
                inverse.append(inverse[MOD % len(inverse)] * (MOD - MOD // len(inverse)) % MOD) 
                inverse_factorial.append(inverse_factorial[-1] * inverse[-1] % MOD)
            return (factorial[n] * inverse_factorial[n - r] % MOD) * inverse_factorial[r] % MOD

        def sieve_of_eratosthenes(limit):  
            prime_numbers = []
            smallest_prime_factor = [-1] * (limit + 1)
            for i in xrange(2, limit + 1):
                if smallest_prime_factor[i] == -1:
                    smallest_prime_factor[i] = i
                    prime_numbers.append(i)
                for prime in prime_numbers:
                    if i * prime > limit or prime > smallest_prime_factor[i]:
                        break
                    smallest_prime_factor[i * prime] = prime
            return prime_numbers

        def get_prime_factors(number):
            factor_count = collections.Counter()
            for prime in prime_list:
                if prime * prime > number:
                    break
                while number % prime == 0:
                    factor_count[prime] += 1
                    number //= prime
            if number != 1:
                factor_count[number] += 1
            return factor_count

        prime_list = sieve_of_eratosthenes(int(maxValue**0.5))
        result = 0
        for current_value in xrange(1, maxValue + 1):
            total_ways = 1
            for count in get_prime_factors(current_value).itervalues():
                total_ways = (total_ways * compute_nCr(length + count - 1, count)) % MOD  
            result = (result + total_ways) % MOD
        return result