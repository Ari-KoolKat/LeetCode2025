class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        data = sorted(nums)
        windows = [] # groups of numbers that are within limits
        add = [] 
        windowsIndex = {} # 
        idx = 0
        for i in range(len(data)):
            if i==0 or data[i]-data[i-1]<=limit:
                add.append(data[i])
            else:
                windows.append(add)
                idx+=1
                add = [data[i]]
            windowsIndex[data[i]] = idx
        windows.append(add)

        counter = [0] * len(windowsIndex)
        for i in range(len(nums)):
            idx = windowsIndex[nums[i]]
            nums[i] = windows[idx][counter[idx]]
            counter[idx]+=1
        return nums