class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp=s[0]
        counter=1
        res=""
        res+=temp
        for i in range(1,len(s)):
            if s[i]==temp:
                if counter>=2:
                    temp=s[i]
                    continue
                counter+=1
            else:
                temp=s[i]
                counter=1
            res+=s[i]
        return res