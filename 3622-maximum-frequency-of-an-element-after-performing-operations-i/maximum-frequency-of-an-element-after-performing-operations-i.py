class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        maxi=max(nums)+1
        freq=[0]*maxi
        for i in nums:
            freq[i]+=1
        ans=0 
        # print(freq) 
        curr=sum(freq[:k])
        # print(curr,k)  
        for i in range(len(freq)):
            if  i-k>0:
                curr-=freq[i-k-1]
            if k+i<len(freq):    
               curr+=freq[k+i]  
            # print(curr)      
            check=min(numOperations,curr-freq[i])
            ans=max(check+freq[i],ans) 
        return ans      
        