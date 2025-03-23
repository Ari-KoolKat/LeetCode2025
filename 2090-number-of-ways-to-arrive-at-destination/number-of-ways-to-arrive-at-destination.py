class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Step 1️⃣: Build the adjacency list for the graph
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        # Step 2️⃣: Initialize arrays to store shortest distance and number of ways
        ways = [0] * n
        ways[0] = 1
        dis = [float("inf")] * n
        dis[0] = 0
        
        # Step 3️⃣: List to store (time, node)
        queue = [[0, 0]]  # (current time, node)
        
        while queue:
            # Single line to find and pop the element with the smallest time
            time, node = min(queue, key=lambda x: x[0])
            queue.remove([time, node])
            #tuples are non-changable and saves memory than lists
            
            # Explore all neighbors of the current node
            for neighbor, travel_time in adj[node]:
                new_time = time + travel_time
                
                # Case 1️⃣: If we found another way with the same shortest time
                if new_time == dis[neighbor]:
                    ways[neighbor] += ways[node]
                
                # Case 2️⃣: If we found a shorter time to reach the neighbor
                elif new_time < dis[neighbor]:
                    dis[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    queue.append([new_time, neighbor])  # Add to the list

        # Step 4️⃣: Return the number of ways to reach the destination modulo 10^9 + 7
        MOD = 10**9 + 7
        return ways[n-1] % MOD