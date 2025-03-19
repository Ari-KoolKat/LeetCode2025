class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        c=0
        for i in range(l-2):
            if nums[i]==0:
                nums[i]=1
                if nums[i+1]==0:
                    nums[i+1]=1
                else:
                    nums[i+1]=0
                if nums[i+2]==0:
                    nums[i+2]=1
                else:
                    nums[i+2]=0
                c+=1
        if nums[l-1]==0 or nums[l-2]==0:
            return -1
        return c