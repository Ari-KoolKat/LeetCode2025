import heapq
from collections import defaultdict

class NumberContainers(object):

    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = defaultdict(list)

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number != number:
                heapq.heappush(self.number_to_indices[number], index)
        
        self.index_to_number[index] = number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.number_to_indices:
            return -1
        
        while self.number_to_indices[number] and self.index_to_number[self.number_to_indices[number][0]] != number:
            heapq.heappop(self.number_to_indices[number])
        
        return self.number_to_indices[number][0] if self.number_to_indices[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)