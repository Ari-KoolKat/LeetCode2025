class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        u = [] #list of users that need help
        for i in friendships: #checking each pair
            a = set(languages[i[0] - 1]) #getting languages person 1 know
            b = set(languages[i[1] - 1]) #same for second 
            c = a.intersection(b) #checking number of common languages
            if len(c) == 0: #if no common language between both friends
                u.append(i)

        users_in_need = set() #users that will need to learn a language
        for i in u:
            users_in_need.add(i[0] - 1) #appending users that couldn't communicate
            users_in_need.add(i[1] - 1)

        mi= float('inf') #for minimum no of operations
        for l in range(1, n + 1): #checking for all languages how many  changes
            r=0 #number of changes needed if language 'l' was to be taught
            for u in users_in_need: # checking for every user
                if l not in languages[u]: 
                    r += 1 #teaching a user langugae
            mi= min(mi, r) #updating minimum
        return mi #returning minimum 