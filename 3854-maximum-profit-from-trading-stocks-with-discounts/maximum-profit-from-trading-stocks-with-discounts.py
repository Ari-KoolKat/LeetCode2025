class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        from sys import setrecursionlimit
        setrecursionlimit(10**7)
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            g[u-1].append(v-1)

        def dfs(u):
            child_dp = [dfs(v) for v in g[u]]

            f0 = [float('-inf')] * (budget+1)
            f1 = [float('-inf')] * (budget+1)
            f0[0] = 0
            f1[0] = 0
            for dp_no_v, dp_yes_v in child_dp:
                new0 = [float('-inf')] * (budget+1)
                new1 = [float('-inf')] * (budget+1)
                for spent in range(budget+1):
                    if f0[spent] > -1e18:
                        for k in range(budget-spent+1):
                            val = f0[spent] + dp_no_v[k]
                            if val > new0[spent+k]:
                                new0[spent+k] = val
                    if f1[spent] > -1e18:
                        for k in range(budget-spent+1):
                            val = f1[spent] + dp_yes_v[k]
                            if val > new1[spent+k]:
                                new1[spent+k] = val
                f0, f1 = new0, new1

            dp_no_u = [float('-inf')] * (budget+1)
            dp_yes_u = [float('-inf')] * (budget+1)

            cost_no  = present[u]
            profit_no = future[u] - cost_no
            cost_yes  = present[u] // 2
            profit_yes = future[u] - cost_yes

            for c in range(budget+1):
                if f0[c] > dp_no_u[c]:
                    dp_no_u[c] = f0[c]
                    dp_yes_u[c] = f0[c]

                if c >= cost_no and f1[c-cost_no] + profit_no > dp_no_u[c]:
                    dp_no_u[c] = f1[c-cost_no] + profit_no
                if c >= cost_yes and f1[c-cost_yes] + profit_yes > dp_yes_u[c]:
                    dp_yes_u[c] = f1[c-cost_yes] + profit_yes

            return dp_no_u, dp_yes_u

        dp_root_no, _ = dfs(0)
        return max(dp_root_no[:budget+1])