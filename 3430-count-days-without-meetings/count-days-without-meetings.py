class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort() 
        curr = 1
        ans = 0
        
        for start, end in meetings:
            if curr < start:
                ans += (start - curr)
            curr = max(curr, end + 1)
        
        if days >= curr:
            ans += (days - curr + 1)

        return ans