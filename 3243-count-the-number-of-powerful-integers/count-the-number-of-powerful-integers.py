class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        s_val = int(s)
        s_len = len(s)
        
        # Check if any digit in s exceeds the limit
        if any(int(c) > limit for c in s):
            return 0
        
        # Check if s_val is larger than finish
        if s_val > finish:
            return 0
        
        # Calculate X_min: the smallest X >= start that ends with s
        ten_pow_s_len = 10 ** s_len
        if start <= s_val:
            X_min = s_val
        else:
            q = (start - s_val - 1) // ten_pow_s_len + 1
            X_min = q * ten_pow_s_len + s_val
        
        # Calculate X_max: the largest X <= finish that ends with s
        X_max = (finish - s_val) // ten_pow_s_len * ten_pow_s_len + s_val
        
        if X_min > X_max:
            return 0
        
        prefix_min = (X_min - s_val) // ten_pow_s_len
        prefix_max = (X_max - s_val) // ten_pow_s_len
        
        def count_less_equal(N):
            if N < 0:
                return 0
            s_N = str(N)
            n = len(s_N)
            # memo[i][tight] : number of ways to choose digits i..n-1, with tight constraint
            memo = {}
            
            def dp(i, tight):
                if i == n:
                    return 1
                key = (i, tight)
                if key in memo:
                    return memo[key]
                max_digit = int(s_N[i]) if tight else limit
                res = 0
                for d in range(0, max_digit + 1):
                    if d > limit:
                        continue
                    new_tight = tight and (d == max_digit)
                    res += dp(i + 1, new_tight)
                memo[key] = res
                return res
            
            return dp(0, True)
        
        return count_less_equal(prefix_max) - count_less_equal(prefix_min - 1)