class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        tasks.sort()  # sort tasks by difficulty (ascending)
        workers.sort()  # sort workers by strength (ascending)
        def canAssign(k):
            """
            Check if we can complete k tasks
            """
            selected_tasks = tasks[:k]  # Take k easiest tasks
            available_workers = workers[-k:]  # Take k strongest workers
            remaining_pills = pills
            
            # Process from hardest to easiest task
            for task in reversed(selected_tasks):
                # If strongest worker can't do task even with pill, return False
                if available_workers[-1] < task and \
                (available_workers[-1] + strength < task or remaining_pills == 0):
                    return False
                
                # If strongest worker can do it without pill, assign them
                if available_workers[-1] >= task:
                    available_workers.pop()  # Use strongest worker
                else:
                    # Find the weakest worker who can do this task with a pill
                    # Binary search to find the right worker
                    left, right = 0, len(available_workers) - 1
                    while left < right:
                        mid = (left + right) // 2
                        if available_workers[mid] + strength >= task:
                            right = mid
                        else:
                            left = mid + 1
                    
                    # Remove this worker and use a pill
                    available_workers.pop(left)
                    remaining_pills -= 1
            
            return True
        
        # Binary search to find maximum k
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if canAssign(mid):
                left = mid
            else:
                right = mid - 1
                
        return left