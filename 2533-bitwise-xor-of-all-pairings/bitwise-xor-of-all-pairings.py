class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result1 = 0
        result2 = 0
        len_1 = len(nums1)
        len_2 = len(nums2)

        for num in nums1:
            result1 ^= num

        for num in nums2:
            result2 ^= num

        if len_1 % 2 == 0:
            result2 = 0

        if len_2 % 2 == 0:
            result1 = 0            

        
        return result1^result2