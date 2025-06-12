class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans= -1
        numsSize=len(nums)
        for i in range(numsSize-1):
            maxa=max(abs(nums[i]-nums[i+1]),abs(nums[i+1]-nums[i]))
            ans=max(ans,maxa)
        
        ans=max(max(abs(nums[0]-nums[numsSize-1]),abs(nums[numsSize-1]-nums[0])),ans)
        return ans