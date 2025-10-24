class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_balanced(x):
            s = str(x)
            if '0' in s:                   
                return False
            cnt = collections.Counter(s)
            for ch, freq in cnt.items():
                if freq != int(ch):        
                    return False
            return True

        cur = n + 1
        while True:                        
            if is_balanced(cur):
                return cur
            cur += 1