class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        m = len(potions)
        res = []
        
        for spell in spells:
            need = float(success) / spell
            idx = bisect.bisect_left(potions, need)
            res.append(m - idx)  
            
        return res