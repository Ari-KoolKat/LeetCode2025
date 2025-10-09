class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n=len(skill) #the number of wizards
        t=[0]*n #this the time by each wiz for a potion 

        for x in mana: #for each Potion!
            t[0] += skill[0] *x  #update the time for the first wiz
            #Important: FORWARD PASS
            for i in range(1,n): 
                t[i] =max(t[i],t[i-1]) + skill[i]*x

            #Backward pass to get ACTUAL time for that potion X
            for i in range(n-2,-1,-1):
                t[i] = t[i+1] - skill[i+1]*x

        #After checking for each Potion
        return t[-1] #Now simply return the last wiz time