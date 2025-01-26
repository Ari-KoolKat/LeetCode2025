class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        n = len(favorite)
        in_degree = [0] * n
        chain_lengths = [0] * n
        visited = [False] * n

        # Calculate in-degrees
        for fav in favorite:
            in_degree[fav] += 1

        # Queue for processing nodes with in-degree of 0
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)

        # Process the graph to calculate chain lengths
        while q:
            node = q.popleft()
            visited[node] = True

            next_node = favorite[node]
            chain_lengths[next_node] = chain_lengths[node] + 1
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)

        max_cycle = 0
        total_chains = 0

        # Detect cycles and calculate their lengths
        for i in range(n):
            if not visited[i]:
                current = i
                cycle_length = 0
                while not visited[current]:
                    visited[current] = True
                    current = favorite[current]
                    cycle_length += 1

                # Special case for cycles of length 2
                if cycle_length == 2:
                    total_chains += 2 + chain_lengths[i] + chain_lengths[favorite[i]]
                else:
                    max_cycle = max(max_cycle, cycle_length)

        # Return the maximum of the longest cycle or total chains
        return max(max_cycle, total_chains)