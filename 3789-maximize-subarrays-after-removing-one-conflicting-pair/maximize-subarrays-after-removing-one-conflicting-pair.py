class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        right = [[] for _ in range(n + 1)]

        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))

        ans = 0
        left = [0, 0]  
        bonus = [0] * (n + 1)

        for r in range(1, n + 1):
            for l in right[r]:
                left = self.maxPair(left, [l, left[0]], [left[0], l])
            ans += r - left[0]
            bonus[left[0]] += left[0] - left[1]

        return ans + max(bonus)

    def maxPair(self, pair1, pair2, pair3):
        max_pair = pair1
        for curr in [pair2, pair3]:
            if curr[0] > max_pair[0] or (curr[0] == max_pair[0] and curr[1] > max_pair[1]):
                max_pair = curr
        return max_pair