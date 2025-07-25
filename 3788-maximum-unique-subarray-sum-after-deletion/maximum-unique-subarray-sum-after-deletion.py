class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        nums=list(nums)
        total=0
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if total+nums[i]>total:
                total+=nums[i]
            else:
                break
        return total if total!=0 else nums[len(nums)-1]