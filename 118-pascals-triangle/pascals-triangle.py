class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr=[[1]]
        if numRows==1:
            return arr
        arr.append([1,1])
        for i in range(2,numRows):
            num=[1]
            j=1
            while(j<len(arr[i-1])):
                ele=arr[i-1][j-1]+arr[i-1][j]
                num.append(ele)
                j+=1
            num.append(1)
            arr.append(num)
        return arr