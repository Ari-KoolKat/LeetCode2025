class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        d=dict()
        for i in range(len(s)):
            d[s[i]]=i
        st,end=0,0
        res=[]
        for i in range(0,len(s)):
            end=max(end,d[s[i]])
            if(i==end):
                res.append(end-st+1)
                st=i+1
        return res