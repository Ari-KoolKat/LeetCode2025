class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        server_count = 0

        def BFS(i, j):
            
            que = deque([(i,j)])
            visited.add((i,j))
            connected_servers = 0

            while que:
                x, y = que.popleft()
                connected_servers += 1

                for col in range(n):
                    if col != y and grid[x][col] == 1 and (x,col) not in visited:
                        que.append((x,col))
                        visited.add((x,col))
                
                for row in range(m):
                    if row != x and grid[row][y] == 1 and (row,y) not in visited:
                        que.append((row,y))
                        visited.add((row,y))
            
            return connected_servers
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    connected = BFS(i,j)

                    if connected > 1:
                        server_count += connected
        
        return server_count