class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c=0
        
        for j in range(len(strs[0])):
            i=0
            while i<len(strs)-1:
                c1=strs[i][j]
                c2=strs[i+1][j]
                if c1>c2:
                    
                    c+=1
                    break
                i+=1
        return c
