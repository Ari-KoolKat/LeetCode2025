class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        strictly_increasing = 1
        strictly_decreasing = 1
        last_indx_of_increase = -1
        last_indx_of_decrease = -1
        current_increase = 1
        current_decrease = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                #strictly increasing
                if last_indx_of_increase == i-1:
                    current_increase +=1
                else:
                    current_increase = 2
                last_indx_of_increase = i
                strictly_increasing = max(strictly_increasing,current_increase)
                current_decrease = 1
            elif nums[i]<nums[i-1]:
                # strictly decreasing
                if last_indx_of_decrease == i-1:
                    current_decrease +=1
                else:
                    current_decrease = 2
                last_indx_of_decrease = i
                strictly_decreasing = max(strictly_decreasing,current_decrease)
                current_increase = 1
        
        return max(strictly_increasing,strictly_decreasing)