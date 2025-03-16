class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        def isrepair(time):
            re = 0
            for i in ranks:
                t = time // i
                re += math.floor(sqrt(t))
            if re>=cars: return True
            return False
        low = 0
        high = max(ranks) * (cars ** 2)
        ans = high
        while low<=high:
            mid = low + (high - low) // 2
            if isrepair(mid):
                ans = min(ans,mid)
                high = mid - 1
            else : low = mid + 1
        return ans