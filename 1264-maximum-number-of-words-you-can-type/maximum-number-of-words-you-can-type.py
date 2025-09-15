class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        a=text.split() #seprating each word
        s=set(brokenLetters) #the set of characters
        c=0 #counting words that can be typed
        for i in a:
            f=True #flag to check was there a broken letter used
            for j in s: #check if any broken letter was used in this
                if j in i: #if yes change flag value
                    f=False
                    break
            if f: #if flag value still True i.e no broken letter
                c+=1
        return c #return total words like this
