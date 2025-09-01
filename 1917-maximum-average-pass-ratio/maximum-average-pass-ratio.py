class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        heap=[ (-((p+1)/float(t+1)-p/float(t)),p*1.0,t*1.0) for p,t in classes]
        heapify(heap)
        for num in range(extraStudents):
            _,p,t=heappop(heap)
            heappush(heap,(-((p+2)/(t+2)-(p+1)/(t+1)),p+1,t+1))
        return sum( p/t for _,p,t in heap)/len(classes)
