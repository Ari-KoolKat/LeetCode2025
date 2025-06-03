class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        total_candies = 0
        have_keys = set()
        have_boxes = set(initialBoxes)
        opened = set()
        queue = deque(initialBoxes)

        while queue:
            box = queue.popleft()
            if status[box] == 0 and box not in have_keys:
                continue
            
            if box in opened:
                continue 
            
            opened.add(box)
            total_candies += candies[box]
            
            for key in keys[box]:
                if key not in have_keys:
                    have_keys.add(key)
                    if key in have_boxes and key not in opened:
                        queue.append(key)
            
            for b in containedBoxes[box]:
                if b not in have_boxes:
                    have_boxes.add(b)
                    queue.append(b)
        
        return total_candies