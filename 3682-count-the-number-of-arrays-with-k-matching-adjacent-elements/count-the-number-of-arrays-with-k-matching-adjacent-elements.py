class Solution(object):
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
    
        MOD = 10**9 + 7

        def factorial(n):
            fac = [1] * (n + 1)
            for i in range(2, n + 1):
                fac[i] = fac[i-1] * i % MOD
            return fac

        def inv(a):
            return pow(a, MOD-2, MOD)

        def comb(n, k, fac):
            return fac[n] * inv(fac[k]) % MOD * inv(fac[n-k]) % MOD

        if k >= n:
          return 0
    
        fac = factorial(n)

        return comb(n-1, k, fac) * m * pow(m-1, n-1-k, MOD) % MOD