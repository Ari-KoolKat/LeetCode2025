class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        def is_close(a, b, tol=1e-9):
            return abs(a - b) < tol

        def dfs(nums):
            if len(nums) == 1:
                return is_close(nums[0], 24)

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                    for op in compute(nums[i], nums[j]):
                        next_nums.append(op)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()
            return False

        def compute(a, b):
            results = [a + b, a - b, b - a, a * b]
            if b != 0:
                results.append(float(a) / b)
            if a != 0:
                results.append(float(b) / a)
            return results

        return dfs(cards)