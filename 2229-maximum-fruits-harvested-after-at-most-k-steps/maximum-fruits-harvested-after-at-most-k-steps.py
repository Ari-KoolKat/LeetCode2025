class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        from bisect import bisect_left, bisect_right

        positions = [pos for pos, _ in fruits]
        prefix_sum = [0]
        for _, amount in fruits:
            prefix_sum.append(prefix_sum[-1] + amount)

        def get_fruit_total(left, right):
            l = bisect_left(positions, left)
            r = bisect_right(positions, right)
            return prefix_sum[r] - prefix_sum[l]

        max_fruits = 0
       
        for steps_left in range(0, k + 1):
            left = startPos - steps_left
            right = startPos + max(0, k - 2 * steps_left)
            if left > right:
                continue
            max_fruits = max(max_fruits, get_fruit_total(left, right))

        for steps_right in range(0, k + 1):
            right = startPos + steps_right
            left = startPos - max(0, k - 2 * steps_right)
            if left > right:
                continue
            max_fruits = max(max_fruits, get_fruit_total(left, right))

        return max_fruits