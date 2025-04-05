class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=[0]
        def find(index,cur):
            cursum=0
            for i in cur:
                cursum^=i
            total[0]+=cursum
            for i in range(index,len(nums)):
                cur.append(nums[i])
                find(i+1,cur)
                cur.pop()
        find(0,[])
        return total[0]