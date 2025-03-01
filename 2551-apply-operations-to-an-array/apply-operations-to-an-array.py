class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Step 1: Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2  # Multiply current element by 2
                nums[i + 1] = 0  # Set the next element to 0

        # Step 2: Shift zeros to the end
        result = []
        for num in nums:
            if num != 0:
                result.append(num)

        # Add zeros to the end of the result
        result.extend([0] * (n - len(result)))

        return result