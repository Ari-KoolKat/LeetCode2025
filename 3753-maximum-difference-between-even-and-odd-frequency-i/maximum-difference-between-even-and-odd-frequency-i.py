class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        
        odd_freqs = [count for count in freq.values() if count % 2 == 1]
        even_freqs = [count for count in freq.values() if count % 2 == 0]
        
        return max(odd_freqs) - min(even_freqs)