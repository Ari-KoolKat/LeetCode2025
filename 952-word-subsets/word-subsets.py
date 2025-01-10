class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        d=defaultdict(int)
        for j in words2:
            t=defaultdict(int)
            for i in j:
                t[i]+=1
            for k in t:
                if k not in d:
                    d[k]=t[k]
                else:
                    d[k]=max(t[k],d[k])
        op=set()
        for i in words1:
            td=d.copy()
            c=1
            for j in i:
                if j in td:
                    td[j]-=1
            for m in td:
                if td[m]>0:
                    c=0
                    break
            if c:
                op.add(i)


        return list(op)