import bisect
class Router(object):
    """    
        maintain a stack - forwarding
        set to maintain duplicates
        destination dict, [timestamp]? 
        when forward, remove it
    """
    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.stack = []
        self.packets = set()
        self.dict = defaultdict(list)
        self.limit = memoryLimit
        

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        tup = (source, destination, timestamp)
        if tup in self.packets:
            return False
        self.packets.add(tup)
        self.stack.append(tup)
        if len(self.stack) > self.limit:
            tup =  self.stack[0]
            self.stack = self.stack[1:]
            self.packets.remove(tup)
         
            # get timestamp of destination
            ts = self.dict[tup[1]]
            ts.remove(tup[2])
            # remove from dict for destination
            self.dict[tup[1]] = ts

        self.dict[destination].append(timestamp)
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if len(self.stack) == 0:
            return []      
        tup = self.stack[0]
        self.packets.remove(tup)
        self.stack = self.stack[1:]

        # get timestamp of destination
        ts = self.dict[tup[1]]
        ts.remove(tup[2])
        
        # remove from dict for destination
        self.dict[tup[1]] = ts
        return [tup[0], tup[1], tup[2]]
        
        

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """


        ts = self.dict[destination]
          
        # Use binary search to find the lower and upper bounds
        left = bisect.bisect_left(ts, startTime)
        right = bisect.bisect_right(ts, endTime)
        
        return right - left
        
        
            
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)