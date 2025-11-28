class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(10**6)

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        self.count = 0

        def dfs(curr, parent):
            visited[curr] = True
            total = values[curr]  # Python int is arbitrary precision
            for nbr in graph[curr]:
                if nbr == parent:
                    continue
                if not visited[nbr]:
                    child_rem = dfs(nbr, curr)
                    total += child_rem  # child_rem is in [0, k-1]
            rem = total % k
            # canonicalize negative remainders (defensive; Python % already non-negative but kept for parity)
            rem = (rem + k) % k
            if rem == 0:
                self.count += 1
            return rem

        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        return self.count