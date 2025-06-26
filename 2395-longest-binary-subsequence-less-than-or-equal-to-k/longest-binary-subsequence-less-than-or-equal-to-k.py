class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        c0 = [0] * n

        # Precompute the number of '0's up to each index
        c0[0] = ord('1') - ord(s[0])  # 1 if s[0] == '0', else 0
        for i in range(1, n):
            c0[i] = c0[i - 1] + (ord('1') - ord(s[i]))

        i = n - 1
        total = 0
        power = 1
        count = 0

        while i >= 0 and total <= k and power <= k:
            if s[i] == '1':
                total += power
            if total <= k:
                count += 1
            power *= 2
            i -= 1

        if i >= 0:
            return count + c0[i]
        else:
            return count