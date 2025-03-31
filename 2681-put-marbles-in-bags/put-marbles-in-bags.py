class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0  
        
        pair_sums = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        pair_sums.sort()

        min_score = sum(pair_sums[:k - 1])
        max_score = sum(pair_sums[-(k - 1):])
        
        return max_score - min_score