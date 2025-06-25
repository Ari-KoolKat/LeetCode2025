class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        def count_pairs(x):
            """Count number of pairs (nums1[i], nums2[j]) where nums1[i] * nums2[j] <= x."""
            count = 0
            for num in nums1:
                if num > 0:
                    # Count nums2[j] <= x / num using binary search
                    count += bisect_right(nums2, x // num)
                if num < 0:
                    # Count nums2[j] >= x / num using binary search
                    count += len(nums2) - bisect_left(nums2, ceil(x/float(num)))# this is python fuckery
                if num == 0 and x >=0:
                    # If num is zero, all products are zero (valid if x >= 0)
                    count += len(nums2)
            return count
        
        # Define search space for the product
        A = [nums1[0], nums1[-1]]
        B = [nums2[0], nums2[-1]]
        cartesian_product = [i*j for i, j in list(itertools.product(A, B))]
        left, right = min(cartesian_product), max(cartesian_product)
        
        while left < right:
            mid = (left + right) // 2
            if count_pairs(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left