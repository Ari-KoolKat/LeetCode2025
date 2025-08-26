class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        dm=0 #diagonal max
        am=0 #area max
        for i,j in dimensions:
            dc=sqrt(i**2+j**2) #current diagonal 
            ac=i*j #current area
            if dc>dm or(dc==dm and ac>am):
                am=ac
                dm=dc
        return am