class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prev_s = set()
        res = set()
        for num in arr:
            cur_s = {num}
            for val in prev_s:
                cur_s.add(val | num)
            prev_s = cur_s
            res.update(cur_s)
        return len(res)