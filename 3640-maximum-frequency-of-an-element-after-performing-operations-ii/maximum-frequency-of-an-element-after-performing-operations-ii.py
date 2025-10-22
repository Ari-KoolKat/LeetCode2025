class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """

        m = max(nums) + k
        d = {}
        f = {}
        for n in nums:
            f[n] = f.get(n, 0) + 1
            l = max(n - k, 0)
            r = min(n + k, m)
            d[l] = d.get(l, 0) + 1
            d[r + 1] = d.get(r + 1, 0) - 1
            if n not in d:
                d[n] = 0
        r = 1
        s = 0
        for t in sorted(d.keys()):
            d[t] += s
            tf = f.get(t, 0)
            c = d[t] - tf
            mp = min(c, numOperations)
            r = max(r, tf + mp)
            s = d[t]
        return r