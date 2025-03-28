class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        k = len(queries)
        result = [0] * k

        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        points_collected = 0
        
        for q_value, q_index in sorted_queries:
            while min_heap and min_heap[0][0] < q_value:
                value, r, c = heapq.heappop(min_heap)
                points_collected += 1

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < m and 0 <= new_c < n and not visited[new_r][new_c]:
                        heapq.heappush(min_heap, (grid[new_r][new_c], new_r, new_c))
                        visited[new_r][new_c] = True

            result[q_index] = points_collected

        return result