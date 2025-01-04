class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_occ = {}
        last_occ = {}
        for i, char in enumerate(s):
            if char not in first_occ:
                first_occ[char] = i 
            last_occ[char] = i
        unique_palindromes = set()
        for char in first_occ:
            start = first_occ[char]
            end = last_occ[char]
            if end - start > 1:
                for middle_char in set(s[start + 1: end]):
                    unique_palindromes.add((char, middle_char, char))
        return len(unique_palindromes)            