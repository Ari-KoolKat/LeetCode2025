class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def backtrack(s):
            if len(s) == n:
                self.count += 1
                if self.count == k:
                    self.result = s
                return

            for c in "abc":
                if not s or s[-1] != c:  # Ensure no adjacent characters are the same
                    backtrack(s + c)
                    if self.result:  # Stop early if we found the k-th string
                        return

        self.count = 0
        self.result = ""

        backtrack("")
        return self.result