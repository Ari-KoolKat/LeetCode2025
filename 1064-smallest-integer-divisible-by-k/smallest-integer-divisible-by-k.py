class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        memo=set()
        remainder = 1
        ans = 1
        while remainder%k!=0:
            remainder = remainder*10+1
            remainder = remainder%k
            if remainder in memo:
                return -1
            else:
                memo.add(remainder)
            ans +=1

        return ans 