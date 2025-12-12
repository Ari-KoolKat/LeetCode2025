class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        sorted_dict=[]
        for index,event in enumerate(events):
            timestamp=int(event[1])
            evetype=0 if event[0]=="OFFLINE" else 1
            sorted_dict.append((timestamp,evetype,index))
        sorted_dict.sort(key=lambda x: (x[0], x[1], x[2]))
        print(sorted_dict)
        mentions=[0]*numberOfUsers
        offline=[0]*numberOfUsers
        for vals in sorted_dict:
            index=vals[2]
            origin=events[index]
            eveType=origin[0]
            if eveType=="OFFLINE":
                id=int(origin[2])
                timestamp=int(origin[1])
                offline[id]=timestamp+60
            else:
                timestamp=int(origin[1])
                menString=origin[2].split()
                for men in menString:
                    if men[0]=='i':
                        id=int(men[2:])
                        mentions[id]+=1
                    if men=="ALL":
                        for k in range(numberOfUsers):
                            mentions[k]+=1
                    if men=="HERE":
                        for k in range(numberOfUsers):
                            if timestamp>=offline[k]:
                                mentions[k]+=1
        return mentions 
