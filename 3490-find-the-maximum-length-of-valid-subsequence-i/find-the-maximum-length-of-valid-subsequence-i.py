class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        v=0
        k=0
        t=0
        y=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                t+=1
            if nums[i]%2==1:
                y+=1
        for i in range(1,len(nums)):
            if (nums[i-1]+nums[i])%2==0 :
                if nums[i-1]%2==0:
                    c+=1
                else:
                    v+=1
            else:
                k+=1
        return max(k+1,v+1,c+1,t,y)