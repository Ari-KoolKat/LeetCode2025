class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # Check for cuts along both axes
        return self.canCut(rectangles, 0) or self.canCut(rectangles, 1)

    def canCut(self, rectangles, axis):
        # Sort rectangles based on the chosen axis
        rectangles.sort(key=lambda rect: rect[axis])

        cuts = 0
        previous_end = -1

        for rect in rectangles:
            start = rect[axis]
            end = rect[axis + 2]

            # Check if we can make a cut
            if start >= previous_end:
                cuts += 1
            previous_end = max(previous_end, end)

            # If we have made 3 or more cuts, return True
            if cuts >= 3:
                return True

        return False   