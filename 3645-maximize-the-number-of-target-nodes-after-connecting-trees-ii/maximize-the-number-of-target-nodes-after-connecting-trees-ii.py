class Solution(object):
    def maxTargetNodes(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: List[int]
        """
        def getcolors(edges):
            n = len(edges) + 1
            neigh = [[] for _ in range(n)]
            for [u,v] in edges:
                neigh[u].append(v)
                neigh[v].append(u)
            queue = deque()
            queue.append(0)
            
            colors = [-1]*n
            colors[0] = 0
            
            while queue:
                index = queue.popleft()
                for nextindex in neigh[index]:
                    if colors[nextindex] >= 0:
                        continue 
                    colors[nextindex] = 1 - colors[index] 
                    queue.append(nextindex)
                    
            return colors
        
        colors1 = getcolors(edges1)
        colors2 = getcolors(edges2)
        
        count2 = [0,0]
        for num in colors2:
            count2[num] += 1
            
        part2 = max(count2)
        
        count1 = [0,0]
        for num in colors1:
            count1[num] += 1
            
        return [count1[colors1[i]] + part2 for i in range(len(edges1)+1)]