class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        meetings.sort(key=lambda x:x[2])

        h=[0]*n
        h[0]=h[firstPerson]=1

        i=0
        while i<len(meetings):
            t=meetings[i][2]
            g={}
            s=set()

            while i<len(meetings) and meetings[i][2]==t:
                x,y,_=meetings[i]
                g.setdefault(x,[]).append(y)
                g.setdefault(y,[]).append(x)
                s.add(x);s.add(y)
                i+=1

            q=[p for p in s if h[p]]
            v=set(q)

            while q:
                u=q.pop()
                for w in g.get(u,[]):
                    if w not in v:
                        v.add(w)
                        q.append(w)

            for p in v:
                h[p]=1

        return [i for i in range(n) if h[i]]