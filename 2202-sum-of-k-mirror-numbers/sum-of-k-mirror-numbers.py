class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def is_k_palindrome(num, base):
            digits = []
            while num > 0:
                digits.append(num % base)
                num //= base
            return digits == digits[::-1]

        def generate_palindromes(length):
            res = []
            half = (length + 1) // 2
            for i in range(10**(half - 1), 10**half):
                s = str(i)
                if length % 2 == 0:
                    full = s + s[::-1]
                else:
                    full = s + s[:-1][::-1]
                res.append(int(full))
            return res

        count = 0
        total = 0
        length = 1

        while count < n:
            for num in generate_palindromes(length):
                if is_k_palindrome(num, k):
                    total += num
                    count += 1
                    if count == n:
                        return total
            length += 1

        return total