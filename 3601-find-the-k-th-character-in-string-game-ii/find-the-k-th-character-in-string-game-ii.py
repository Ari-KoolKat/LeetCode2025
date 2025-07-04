class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        L = 1 << len(operations)
        operations = operations[::-1]
        c = 0
        
        for n in operations:
            if k > (L//2):
                k -= (L//2)
				
                if n:
                    c += 1 
            
            L = L//2
        x  = ord("a") + (c %26)
        return chr(x)