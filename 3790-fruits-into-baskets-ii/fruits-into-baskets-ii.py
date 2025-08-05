class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        c=0
        for i in fruits:
            f = False
            for num in baskets:
                if num>= i:
                    baskets.remove(num)
                    f=True
                    break
            if not f:
                c += 1
        return c