class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        minHeap = []

        # Add all boundary cells to the min-heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        waterTrapped = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

        while minHeap:
            height, x, y = heapq.heappop(minHeap)

            # Explore neighbors
            for dx, dy in directions:
                newX, newY = x + dx, y + dy

                # Check bounds
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY]:
                    # If the neighbor is lower than the current height, it can trap water
                    if heightMap[newX][newY] < height:
                        waterTrapped += height - heightMap[newX][newY]
                    
                    # Push the maximum height to the heap
                    heapq.heappush(minHeap, (max(height, heightMap[newX][newY]), newX, newY))
                    visited[newX][newY] = True

        return waterTrapped