class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Helper function to generate all valid row configurations
        def generate_valid_rows(m):
            colors = [0, 1, 2]  # 0: red, 1: green, 2: blue
            valid_rows = []
            
            def backtrack(row):
                if len(row) == m:
                    valid_rows.append(tuple(row))
                    return
                for color in colors:
                    if not row or row[-1] != color:  # Ensure no two adjacent cells are the same
                        row.append(color)
                        backtrack(row)
                        row.pop()
            
            backtrack([])
            return valid_rows
        
        # Generate all valid row configurations for m
        valid_rows = generate_valid_rows(m)
        num_configs = len(valid_rows)
        
        # Precompute transitions between row configurations
        transitions = [[] for _ in range(num_configs)]
        for i in range(num_configs):
            for j in range(num_configs):
                # Check if row i can transition to row j
                if all(valid_rows[i][k] != valid_rows[j][k] for k in range(m)):
                    transitions[i].append(j)
        
        # Initialize the DP table
        dp = [[0] * num_configs for _ in range(n)]
        
        # Base case: first column can be any valid configuration
        for i in range(num_configs):
            dp[0][i] = 1
        
        # Fill the DP table
        for j in range(1, n):
            for i in range(num_configs):
                for prev in transitions[i]:
                    dp[j][i] = (dp[j][i] + dp[j-1][prev]) % MOD
        
        # Sum all ways to color the grid up to column n-1
        result = sum(dp[n-1][i] for i in range(num_configs)) % MOD
        
        return result