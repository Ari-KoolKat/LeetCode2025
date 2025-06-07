class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        freq = defaultdict(list)  

        for i, ch in enumerate(s):
            if ch == '*':
                min_char = min(freq)
                index = freq[min_char].pop()
                stack[index] = None
                if not freq[min_char]:
                    del freq[min_char]
            else:
                freq[ch].append(len(stack))
                stack.append(ch)

        return ''.join(ch for ch in stack if ch is not None)