class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0] * 40
        max_size = 0
        ans = 0

        for i in range(1, n + 1):
            digit_sum = sum(int(c) for c in str(i))
            count[digit_sum] += 1
            if count[digit_sum] > max_size:
                max_size = count[digit_sum]
                ans = 1
            elif count[digit_sum] == max_size:
                ans += 1

        return ans