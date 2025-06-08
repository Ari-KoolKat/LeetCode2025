class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        def dfs(current):
            if current > n:
                return
            result.append(current)
            dfs(current * 10)
            if current % 10 != 9:
                dfs(current + 1)

        dfs(1)
        return result