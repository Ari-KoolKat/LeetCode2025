class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        from collections import defaultdict

        n = len(fruits)
        mp = defaultdict(int)
        i = 0
        j = 0
        count = 0

        while j < n:
            mp[fruits[j]] += 1

            while len(mp) > 2:
                mp[fruits[i]] -= 1
                if mp[fruits[i]] == 0:
                    del mp[fruits[i]]
                i += 1

            count = max(count, j - i + 1)
            j += 1

        return count