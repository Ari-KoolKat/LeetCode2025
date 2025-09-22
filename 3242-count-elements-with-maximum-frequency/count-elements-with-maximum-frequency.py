class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={} #hashMap to store freq of all
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        m_freq=0 #for max frequency in the hashmap
        for i in h:
            if h[i]>m_freq:
                m_freq=h[i]
        r=0 #for result
        for i in h: 
            if h[i]==m_freq: # elements with freq == max freq
                r+=h[i]
        return r # return the toatl elements having max frequency