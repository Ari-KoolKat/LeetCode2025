class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        t = 0
        l = 0
        for r in range(1, len(colors)):
            if colors[r] != colors[l]:
                l = r
            else:
                if neededTime[l] < neededTime[r]:
                    t += neededTime[l]
                    l = r
                else:
                    t += neededTime[r]
        return t