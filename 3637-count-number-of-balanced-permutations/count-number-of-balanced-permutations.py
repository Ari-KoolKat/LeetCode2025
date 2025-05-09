class Solution:
    MOD = 10**9 + 7         # Modulo value for large numbers
    MAXN = 85               # Maximum length based on constraints
    fac = [0] * MAXN        # Arrays to store factorials
    inv = [0] * MAXN        # Arrays to store their modular inverses

    # Precompute factorials and their inverses
    def initComb(self):
        self.fac[0] = 1
        for i in range(1, self.MAXN):
            self.fac[i] = self.fac[i - 1] * i % self.MOD
        self.inv[self.MAXN - 1] = self.modpow(self.fac[self.MAXN - 1], self.MOD - 2)
        for i in range(self.MAXN - 2, -1, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.MOD

    # Calculates a^b mod MOD using binary exponentiation
    def modpow(self, a, b):
        res = 1
        a %= self.MOD
        while b > 0:
            if b & 1:
                res = res * a % self.MOD
            a = a * a % self.MOD
            b >>= 1
        return res

    # Combination C(n, k) with modulo
    def C(self, n, k):
        if k < 0 or k > n:
            return 0
        return self.fac[n] * self.inv[k] % self.MOD * self.inv[n - k] % self.MOD

    # Main function to count balanced permutations
    def countBalancedPermutations(self, num):
        n = len(num)                     # Length of the input string
        digitCount = [0] * 10            # Count of each digit from 0 to 9
        for c in num:
            digitCount[int(c)] += 1
        
        halfLength = n // 2              # Half of the string length
        totalSum = 0                     # Total sum of all digits
        for i in range(10):
            totalSum += digitCount[i] * i
        
        # Return 0 if total sum is not even
        if totalSum % 2 != 0:
            return 0
        targetSum = totalSum // 2        # Target sum for even and odd indices
        
        self.initComb()                  # Initialize combinations

        # Initialize the DP table for storing the number of ways
        prev = [[0] * (halfLength + 1) for _ in range(targetSum + 1)]
        prev[0][0] = 1
        
        usedDigits = 0                   # Number of digits used so far
        for d in range(10):
            if digitCount[d] == 0:
                continue  # Skip digits not present
            
            curr = [[0] * (halfLength + 1) for _ in range(targetSum + 1)]

            for sum_ in range(targetSum + 1):
                for odd in range(halfLength + 1):
                    ways = prev[sum_][odd]
                    if ways == 0:
                        continue

                    # Try placing 'j' digits 'd' on odd indices
                    for j in range(digitCount[d] + 1):
                        k = digitCount[d] - j  # Number of digits on even indices
                        newOdd = odd + j
                        newEven = usedDigits - odd + k
                        
                        # Ensure new counts don't exceed half lengths
                        if newOdd > halfLength or newEven > n - halfLength:
                            continue
                        newSum = sum_ + j * d
                        if newSum > targetSum:
                            continue
                        
                        # Calculate and add new combinations
                        add = ways * self.C(odd + j, j) % self.MOD
                        add = add * self.C(usedDigits - odd + k, k) % self.MOD
                        curr[newSum][newOdd] = (curr[newSum][newOdd] + add) % self.MOD
                    
            usedDigits += digitCount[d]
            prev, curr = curr, prev  # Move to current state for next digit

        return prev[targetSum][halfLength]  # Return the final count of balanced permutations