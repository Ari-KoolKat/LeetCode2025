class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        
        adj = defaultdict(list)
        cost = {}
        group = [-1] * n
        visited = [False] * n
        color = 0

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dfs(node, col):
            if visited[node]: return
            visited[node] = True
            group[node] = col
            for neighbor, weight in adj[node]:
                dfs(neighbor, col)
                cost[col] = cost.get(col, weight) & weight

        for i in range(n):
            if not visited[i]:
                dfs(i, color)
                color += 1

        return [cost[group[u]] if group[u] == group[v] else -1 for u, v in query]