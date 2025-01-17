class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        total = 0
        # Calculate the XOR of all elements in the derived array
        for num in derived:
            total ^= num  # XOR operation
        
        # A valid original array exists if the total XOR is 0
        return total == 0