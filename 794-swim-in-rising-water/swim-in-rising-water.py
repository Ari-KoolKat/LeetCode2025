class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = grid[0][0]
        n,m = len(grid),len(grid[0])
        heap = [(grid[0][0],0,0)]
        dires = [(0,1),(0,-1),(1,0),(-1,0)]
        visited =set()
        visited.add((0,0))
        while heap:
            h,i,j = heapq.heappop(heap)
            ans = max(ans,h)
            if i==n-1 and j==m-1: break
            for di,dj in dires:
                ni,nj = i+di,j+dj
                if 0<=ni<n and 0<=nj<m and (ni,nj) not in visited:
                    heapq.heappush(heap,(grid[ni][nj],ni,nj))
                    visited.add((ni,nj))

        return ans