class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        a, b, c = -1, -1, -1
        count = 0

        for i in range(len(s)):
            if s[i] == 'a':
                a = i
            elif s[i] == 'b':
                b = i
            elif s[i] == 'c':
                c = i

            count += min(a, b, c) + 1
        
        return count