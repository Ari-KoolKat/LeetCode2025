class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        c=0
        for i in range(0,len(nums),3):
            if len(set(nums[i:]))==l-i:
                break
            else:
                c+=1
        return c