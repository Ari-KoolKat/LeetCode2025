class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            sm=0
            cpy=i
            while i:
                sm+=i%10
                i=i/10
            if sm in dic:
                if cpy>dic[sm][1]:
                    dic[sm][0]=dic[sm][1]
                    dic[sm][1]=cpy
                elif cpy>dic[sm][0]:
                    dic[sm][0]=cpy
            else:
                dic[sm]=[-1,cpy]
        mx=-1
        for i in dic:
            if dic[i][0]==-1:
                continue
            mx=max(mx,dic[i][0]+dic[i][1])
        return mx