class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        s=list(s)
        for i in s:
            if i in {'a', 'e', 'i', 'o','u','A','E','I','O','U'}:
                l.append(i)
        l.sort() 
        j=0
        for i in range(len(s)):
            if s[i] in {'a', 'e', 'i', 'o','u','A','E','I','O','U'}: 
                s[i]=l[j]
                j+=1
        return ''.join(s) 