class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        dp = [(1, -1) for _ in range(n)]  
        max_len = 1
        max_index = 0

        def hamming_is_one(a, b):
            if len(a) != len(b):
                return False
            mismatch = 0
            for x, y in zip(a, b):
                if x != y:
                    mismatch += 1
                    if mismatch > 1:
                        return False
            return mismatch == 1

        for j in range(1, n):
            for i in range(j):
                if groups[i] == groups[j]:
                    continue
                if not hamming_is_one(words[i], words[j]):
                    continue
                if dp[i][0] + 1 > dp[j][0]:
                    dp[j] = (dp[i][0] + 1, i)
                    if dp[j][0] > max_len:
                        max_len = dp[j][0]
                        max_index = j

        res = []
        idx = max_index
        while idx != -1:
            res.append(words[idx])
            idx = dp[idx][1]

        return res[::-1]