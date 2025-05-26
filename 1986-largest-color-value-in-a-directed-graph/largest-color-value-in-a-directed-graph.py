class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        # Build graph and indegree
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Initialize dp array for each node and each color (26 colors)
        dp = [[0] * 26 for _ in range(n)]

        # Initialize queue for topological sort
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
            dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_color_value = 0

        # Topological sort and DP
        while queue:
            u = queue.pop(0)
            visited += 1
            for v in graph[u]:
                for c in range(26):
                    count = dp[u][c] + (1 if c == ord(colors[v]) - ord('a') else 0)
                    if count > dp[v][c]:
                        dp[v][c] = count
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
            max_color_value = max(max_color_value, max(dp[u]))

        # Check for cycle
        return max_color_value if visited == n else -1