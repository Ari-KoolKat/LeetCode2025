class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() #sort the array so we get at last
        for i in range(len(nums)-1,1,-1): #loop to traverse the array 
            a=nums[i] #putting elements in triplet
            b=nums[i-1]
            c=nums[i-2]
            if b+c>a: #no need to check other 2 as (a)>(b and c) nums is sorted
                return a+b+c #First condition we get true will be max perimeter
        return 0 #return no valid triangle can be formed by these sides in nums
        