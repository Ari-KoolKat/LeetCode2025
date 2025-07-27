class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#Remove the duplicate neighbour 
        arr=[nums[0]]
        for i in nums:
            if arr[-1]!=i:
                arr.append(i)
        n=len(arr)
#Return if length less than 3
        if n<3:
            return 0

#Count variable initialization
        count=0

#Traverse the array from 1 to length-1
        for i in range(1,n-1):
        #check for valley
            if arr[i-1]>arr[i] and arr[i+1]>arr[i]:
                count+=1
        #check for hill
            elif arr[i-1]<arr[i] and arr[i+1]<arr[i]:
                count+=1

#Return the count of hill and valley
        return count