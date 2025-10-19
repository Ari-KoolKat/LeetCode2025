class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        best = s
        queue = deque([s])
        visited = set()

        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            best = min(best, curr)

            temp = list(curr)
            for i in range(1, len(s), 2):
                temp[i] = str((int(temp[i]) + a)%10)
            added = "".join(temp)
            queue.append(added)

            rotated = curr[b:] + curr[:b]
            queue.append(rotated)
    
        return best