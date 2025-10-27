class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        n = []
        for i in bank:
            c = i.count('1')
            if c:
                n.append(c)
        
        r = 0
        for i in range(len(n) - 1):
            r += n[i] * n[i+1]
        
        return r