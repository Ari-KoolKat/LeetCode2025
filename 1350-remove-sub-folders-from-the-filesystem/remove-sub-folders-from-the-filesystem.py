class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        ans=[folder[0]]
        n=len(folder)
        for i in range(1,n):
            if not folder[i].startswith(ans[-1]+'/'):
                ans.append(folder[i])
        return ans