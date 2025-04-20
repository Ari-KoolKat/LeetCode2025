class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(answers)
        result = 0

        for x, freq in count.items():
            group_size = x + 1
            groups = (freq + group_size - 1) // group_size  # ceiling division
            result += groups * group_size

        return result