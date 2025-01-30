class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs_check_levels(node):
            queue = deque([(node, 0)])
            levels = {}
            max_level = 0
            levels[node] = 0
            
            while queue:
                current, level = queue.popleft()
                
                for neighbor in graph[current]:
                    if neighbor not in levels:
                        levels[neighbor] = level + 1
                        max_level = max(max_level, level + 1)
                        queue.append((neighbor, level + 1))
                    elif (level + 1) % 2 == levels[neighbor] % 2:
                        continue
                    else:
                        return -1  
            
            return max_level + 1
        
        visited = [False] * (n + 1)
        total_groups = 0
        
        for i in range(1, n + 1):
            if visited[i]:
                continue
            
            queue = deque([i])
            visited[i] = True
            component = [i]
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        component.append(neighbor)
            
            max_level = 0
            for node in component:
                levels = bfs_check_levels(node)
                if levels == -1:
                    return -1
                max_level = max(max_level, levels)
            
            total_groups += max_level
        
        return total_groups