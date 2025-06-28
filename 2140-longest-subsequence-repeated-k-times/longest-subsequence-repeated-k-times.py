class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def is_k_subsequence(seq, s, k):
            it = iter(s)
            return all(char in it for char in seq * k)

        char_count = Counter(s)
        candidates = [char for char, count in char_count.items() if count >= k]
        
        queue = deque([""])  
        result = ""
        max_len = len(s) // k
        
        while queue:
            curr_seq = queue.popleft()
            for char in candidates:
                new_seq = curr_seq + char
                if len(new_seq) > max_len:
                    continue
                if is_k_subsequence(new_seq, s, k):
                    if len(new_seq) > len(result) or (len(new_seq) == len(result) and new_seq > result):
                        result = new_seq
                    queue.append(new_seq)
        
        return result