class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        stack = []
        
        for num in nums:
            stack.append(num)
            
            # Keep merging while top two are non-coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g > 1:   # non-coprime
                    merged = lcm(a, b)
                    stack.pop()
                    stack.pop()
                    stack.append(merged)
                else:
                    break
        
        return stack
