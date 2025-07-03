class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = ['a']
        
        while len(word) < k:
            current_length = len(word)
            for i in range(current_length):
                c = word[i]
                if c == 'z':
                    word.append('a')
                else:
                    word.append(chr(ord(c) + 1))
                if len(word) >= k:
                    break

        return word[k - 1]