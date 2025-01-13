class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        for i in s:
            counter[i] = 1 + counter.get(i, 0)
        result = len(s)
        for i in counter:
            #for every three characters we delete 2 characters from the result
            if counter[i]>=3:
                if counter[i]%2 == 0:
                    result-=counter[i]-2    #if a letter has even frequency and greater than 3, then at last only 2 elements will be left.
                else:
                    result-=counter[i]-1    #if a letter has odd frequency and greater than or equals to3, then at last only 1 element will be left.
        return result