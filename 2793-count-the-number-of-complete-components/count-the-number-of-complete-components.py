class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        complete_count = 0

        # Step 2: Find connected components using DFS
        def dfs(node, component):
            stack = [node]
            visited.add(node)
            while stack:
                curr = stack.pop()
                component.append(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        # Step 3: Iterate over all nodes and find connected components
        for i in range(n):
            if i not in visited:
                component = []
                dfs(i, component)

                # Step 4: Check if the component is complete
                size = len(component)
                edge_count = sum(len(graph[node]) for node in component) // 2  # Each edge counted twice
                if edge_count == (size * (size - 1)) // 2:
                    complete_count += 1

        return complete_count