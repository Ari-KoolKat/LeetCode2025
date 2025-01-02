class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(words)
        prefix_sum = [0] * (n + 1)  # Prefix sum array

        # Define a set of vowels for easy checking
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Fill the prefix sum array
        for i in range(n):
            # Check if the current word starts and ends with a vowel
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i + 1] = prefix_sum[i] + 1  # Increment count
            else:
                prefix_sum[i + 1] = prefix_sum[i]  # Carry forward the count

        ans = []  # Result array
        # Answer each query
        for li, ri in queries:
            ans.append(prefix_sum[ri + 1] - prefix_sum[li])  # Calculate the count in range

        return ans  # Return the result