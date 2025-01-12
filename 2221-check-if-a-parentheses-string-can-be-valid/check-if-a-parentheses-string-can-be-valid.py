class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        opc,csc,loc=0,0,0 #opc open count , loc=locked count, csc close count
        for i in range(len(s)):
            if locked[i]=="1" and s[i]=="(":
                opc+=1
            elif locked[i]=="1" and s[i]==")":
                csc+=1
            if locked[i]=="0":
                loc+=1
            if opc+loc<csc:
                return False
        opc,csc,loc=0,0,0
        for i in range(len(s),-1,-1):
            if locked[i-1]=="1" and s[i-1]=="(":
                opc+=1
            elif locked[i-1]=="1" and s[i-1]==")":
                csc+=1
            if locked[i-1]=="0":
                loc+=1
            if csc+loc<opc:
                return False
        return True