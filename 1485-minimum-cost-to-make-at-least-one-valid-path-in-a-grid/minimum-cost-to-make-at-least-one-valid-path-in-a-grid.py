class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l, r = len(grid), len(grid[0]) 
        
        move = {1 : (0,1), 2: (0,-1), 3: (1,0), 4: (-1,0)}
        
        route = [(0,0)]
        
        visited = set()
        k = 0
        while route:
            next_round = []
            for x, y in route:
                while True: 
                    
                    if (x,y) in visited:
                        break
                    if x == l-1 and y == r-1:
                        return k
                    visited.add((x,y))
                    next_round.append((x,y))
                    next_x, next_y = x + move[grid[x][y]][0], y + move[grid[x][y]][1]
                    if 0 <= next_x < l and 0 <= next_y < r and (next_x, next_y) not in visited:
                        x, y = next_x, next_y
                    else:
                        break
            rotate = []
            for x, y in next_round:
                for i, j in [(0,1), (1,0), (-1,0), (0,-1)]:
                    next_x, next_y = x+i, y+j
                    if 0 <= next_x < l and 0 <= next_y < r and (next_x, next_y) not in visited:
                        rotate.append((next_x, next_y))
            route = rotate
            k +=1
        return