class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] == words[j][0:len(words[i])] and words[i] == words[j][-len(words[i])::]:
                    count+=1

        return count