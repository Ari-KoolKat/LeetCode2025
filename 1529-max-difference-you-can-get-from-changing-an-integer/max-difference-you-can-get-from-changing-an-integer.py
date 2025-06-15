class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)

        # Step 1: Maximize the number
        max_chars = list(s)
        for c in max_chars:
            if c != '9':
                x = c
                max_chars = ['9' if ch == x else ch for ch in max_chars]
                break
        max_val = int(''.join(max_chars))

        # Step 2: Minimize the number
        min_chars = list(s)
        if min_chars[0] != '1':
            x = min_chars[0]
            min_chars = ['1' if ch == x else ch for ch in min_chars]
        else:
            for i in range(1, len(min_chars)):
                if min_chars[i] != '0' and min_chars[i] != '1':
                    x = min_chars[i]
                    min_chars = ['0' if ch == x else ch for ch in min_chars]
                    break
        min_val = int(''.join(min_chars))

        return max_val - min_val