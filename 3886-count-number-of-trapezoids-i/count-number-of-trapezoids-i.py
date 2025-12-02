class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        mp = {}

        # Group points by y-coordinate
        for x, y in points:
            if y not in mp:
                mp[y] = []
            mp[y].append(x)

        total = 0

        # Compute total C(s,2)
        for y in mp:
            s = len(mp[y])
            total += s * (s - 1) // 2

        ans = 0

        # Subtract per row and accumulate
        for y in mp:
            s = len(mp[y])
            curr = s * (s - 1) // 2
            total -= curr
            ans = (ans + (curr % MOD) * (total % MOD)) % MOD

        return ans