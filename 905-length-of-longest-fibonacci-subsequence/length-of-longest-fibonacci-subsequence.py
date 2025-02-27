class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_set = set(arr)
        max_lenght = 0

        for i in range(len(arr_set)):
            for j in range(i+1,len(arr_set)):
                a = arr[i]
                b = arr[j]
                lenght = 2

                while a + b in arr_set:
                    a , b = b , a+b
                    lenght += 1

                max_lenght = max(max_lenght, lenght)

        return max_lenght if max_lenght >= 3 else 0