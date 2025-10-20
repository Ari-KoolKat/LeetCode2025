class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        r = 0
        for i in operations:
            if i == '++X' or i == 'X++':
                r += 1
            else:
                r -= 1
        return r