class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        n = len(pattern)
        stack = []
        result = []

        # We need to push digits from '1' to 'n + 1'
        for i in range(1, n + 2):
            stack.append(str(i))  # Push the current digit as a string

            # If we reach the end of the pattern or the next character is 'I'
            if i == n + 1 or pattern[i - 1] == 'I':
                # Pop all elements from the stack and add to the result
                while stack:
                    result.append(stack.pop())

        # Convert the result list to a string
        return ''.join(result)