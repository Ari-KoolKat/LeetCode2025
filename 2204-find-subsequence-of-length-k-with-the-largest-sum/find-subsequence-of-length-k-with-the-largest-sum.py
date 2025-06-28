class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Pair each number with its index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value descending
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        
        # Take top k elements
        top_k = indexed_nums[:k]
        
        # Sort selected k elements by original index to maintain order
        top_k.sort(key=lambda x: x[1])
        
        # Extract values
        return [num for num, i in top_k]