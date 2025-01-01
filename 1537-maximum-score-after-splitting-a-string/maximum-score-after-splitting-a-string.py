class Solution(object):
        
    def countallOnes(self,string):
        count = 0
        for i in string:
            if i == "1":
                count+=1
        return count
    
    
    
    def maxScore(self, s):
        all_one = self.countallOnes(s)
        leftzerosum = 0
        rightzerosum = all_one
        max_score = 0
        
        for i in range(len(s)-1):
            if s[i] == "0":
                leftzerosum+=1
            if s[i] == "1":
                rightzerosum-=1
            max_score = max(max_score , leftzerosum+rightzerosum)
        return max_score