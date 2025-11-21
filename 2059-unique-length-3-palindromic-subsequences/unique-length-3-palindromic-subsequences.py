class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        
        # Loop through each lowercase letter
        for ch in set(s):  # Only consider characters that exist in 's'
            first = s.find(ch)  # Find the first occurrence of the character
            last = s.rfind(ch)  # Find the last occurrence of the character
            
            if first != -1 and last != -1 and first < last:
                # Use a set to find unique characters between first and last
                ans += len(set(s[first + 1:last]))
        
        return ans