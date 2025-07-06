class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1,self.nums2=nums1,nums2
        self.count2=Counter(nums2)


    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        new=self.nums2[index]+val
        self.count2[self.nums2[index]]-=1
        if self.count2[self.nums2[index]]==0: del self.count2[self.nums2[index]]
        self.count2[new]+=1
        self.nums2[index]=new
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        ans=0
        for a in self.nums1:
            comple=tot-a 
            ans+=self.count2.get(comple,0)
        
        return ans