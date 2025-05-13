class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        Count=[0 for i in range(26)]
        a = ord("a")
        for i in s:
            Count[ord(i)-a]+=1
        for i in range(t):
            Count.insert(0, Count.pop(-1))
            Count[1]+= Count[0]
        return sum(Count)%(10**9 +7)      