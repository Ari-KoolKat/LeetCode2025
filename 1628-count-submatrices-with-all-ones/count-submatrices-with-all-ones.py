class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        t=0
        r=len(mat)
        l=len(mat[0])
        a_nums=[]
        for i in range(r):
            nums=[]
            for j in range(l):
                if mat[i][j]==0:
                    nums.append(0)
                elif j==0:
                    nums.append(1)
                else:
                    nums.append(nums[-1]+1)
            a_nums.append(nums)
            for j in range(l):
                min_len=nums[j]
                for k in range(i,-1,-1):
                    min_len=min(min_len,a_nums[k][j])
                    if min_len==0:
                        break
                    t+=min_len
        return t