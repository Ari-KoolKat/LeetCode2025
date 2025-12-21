class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_len = len(strs[0])
        ans = 0
        sorted_pair = [False] * (len(strs) - 1)
        
        for i in range(max_len):
            test = 0
            update = []
            for j in range(len(strs) - 1):
                if not sorted_pair[j] and strs[j][i] > strs[j+1][i]:
                    # print(i,j)
                    ans += 1
                    if test:
                        for u in update:
                            sorted_pair[u] = False
                    # test = 0
                    break
                elif not sorted_pair[j] and strs[j][i] < strs[j+1][i]:
                    test = 1
                    sorted_pair[j] = True
                    update.append(j)
        
        return ans
                