class Solution(object):
    def minOperations(self, boxes):
        n=len(boxes)
        res=[0]*n
        for i in range(n):
            for j in range(n):
                if boxes[j]=='1':
                    res[i]+=abs(i-j)
        return res
        """
        :type boxes: str
        :rtype: List[int]
        """