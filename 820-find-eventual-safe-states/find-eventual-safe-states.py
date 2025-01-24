class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        safe = set()
        for i, row in enumerate(graph):
            if not row:
                safe.add(i)

        visited = set()
        for n in safe:
            visited.add(n)

        def trav(i):
            visited.add(i)
            for n in graph[i]:
              if n not in visited:
                 trav(n)
              if n not in safe:
                    return
            safe.add(i)
        for i in range(len(graph)):
          if i not in visited:
            trav(i)
        return sorted(list(safe))