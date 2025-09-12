class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return any(ch in vowels for ch in s)