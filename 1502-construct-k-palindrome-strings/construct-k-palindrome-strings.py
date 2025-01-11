class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict
        ls = len(s)
        if ls < k:
            return False
        freq = defaultdict(int)
        for elem in s:
            freq[elem] += 1
        odd_freq_cnt = 0
        for elem in freq.keys():
            if freq[elem] % 2 == 1:
                odd_freq_cnt += 1
        if odd_freq_cnt > k:
            return False
        return True