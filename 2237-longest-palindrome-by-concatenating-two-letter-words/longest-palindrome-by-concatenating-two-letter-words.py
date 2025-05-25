class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter

        # Step 1: Count word frequencies
        count = Counter(words)
        length = 0
        has_center = False

        # Step 2: Process reversible pairs
        for word in list(count.keys()):
            rev = word[::-1]
            if word != rev and count[word] > 0 and count[rev] > 0:
                pair = min(count[word], count[rev])
                length += pair * 4
                count[word] -= pair
                count[rev] -= pair

        # Step 2 (continued): Process palindromic words
        for word in count:
            if word[0] == word[1] and count[word] > 0:
                pair = count[word] // 2
                length += pair * 4
                if count[word] % 2 == 1:
                    has_center = True

        # Step 3: Add center if needed
        if has_center:
            length += 2

        # Step 4: Return result
        return length