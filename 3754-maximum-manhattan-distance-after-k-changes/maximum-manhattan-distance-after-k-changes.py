class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def calc(a, b):
            ans = mx = cnt = 0
            for c in s:
                if c == a or c == b:
                    mx += 1
                elif cnt < k:
                    cnt += 1
                    mx += 1
                else:
                    mx -= 1
                ans = max(ans, mx)
            return ans
        
        se = calc('S', 'E')
        sw = calc('S', 'W') 
        ne = calc('N', 'E')
        nw = calc('N', 'W')
        
        return max(se, sw, ne, nw)