class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        n = len(edges)
        parent = [i for i in range(n+1)] # Parent array (1-based indexing)
        rank = [1] * (n + 1) # Rank array for union by rank

        # Find function with path compression
        def find(X):
            if parent[X] != X:
                parent[X] = find(parent[X])
            return parent[X]

        # Union function with union by rank
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False # Cycle detected
            
            # Union by rank
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            
            return True # Successfully merged
        
        # Process each edge
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        
        return []