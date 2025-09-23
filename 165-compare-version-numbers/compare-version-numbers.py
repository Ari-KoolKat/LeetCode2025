class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1=version1.split('.') # Seprating the string by '.'
        v2=version2.split('.')
        l1=len(v1) #checking if both string have equal no division
        l2=len(v2)
        if l1!=l2: #Fixing the imbalance
            if l1>l2:
                for _ in range(l1-l2):
                    v2.append('0')
            else:
                for _ in range(l2-l1):
                    v1.append("0")
        for i in range(len(v1)): #Traversing over each and comparing 
            n1=int(v1[i]) #convert str to int
            n2=int(v2[i])
            if n1>n2: #checking the given conditions
                return 1
            if n1<n2:
                return -1
        return 0 #when both versions are same