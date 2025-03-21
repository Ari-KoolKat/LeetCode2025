class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        in_degree = {}  
        graph = defaultdict(list)  
        
        for r, ing in zip(recipes, ingredients):
            in_degree[r] = len(ing) 
            for item in ing:
                graph[item].append(r)  

        queue = deque(supplies) 
        result = []

        while queue:
            item = queue.popleft()
            if item in in_degree:  
                result.append(item)

            for recipe in graph[item]:  
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0: 
                    queue.append(recipe)

        return result