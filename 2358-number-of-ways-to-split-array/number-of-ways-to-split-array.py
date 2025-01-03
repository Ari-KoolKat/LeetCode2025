class Solution(object):
    def waysToSplitArray(self, nums):
        n = len(nums)
        sumArray = sum(nums)
        validSplits = 0
        sumRight = 0
        sumLeft = 0

        for i in range(n - 1):
            sumLeft = nums[i] + sumLeft
            sumRight = sumArray - sumLeft

            if sumLeft >= sumRight:
                validSplits += 1

        return validSplits