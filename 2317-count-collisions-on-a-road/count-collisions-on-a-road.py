class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        r = directions.lstrip('L').rstrip('R')
        return len(r) - r.count('S')