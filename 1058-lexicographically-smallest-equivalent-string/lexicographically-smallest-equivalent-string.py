class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rootX < rootY:
                    parent[rootY] = rootX
                else:
                    parent[rootX] = rootY

        for a, b in zip(s1, s2):
            union(a, b)

        return "".join(find(c) for c in baseStr)