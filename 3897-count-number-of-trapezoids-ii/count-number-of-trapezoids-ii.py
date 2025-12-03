def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        slope_map = {}
        mid_map   = {}
        
        for i in range(n):
            x_i, y_i = points[i]
            for j in range(i+1, n):
                x_j, y_j = points[j]
                
                dx = x_j - x_i
                dy = y_j - y_i
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                slope = (dx, dy)
    
                c = dx*y_i - dy*x_i
                cmap = slope_map.get(slope)
                if cmap is None:
                    slope_map[slope] = {c: 1}
                else:
                    cmap[c] = cmap.get(c, 0) + 1
                
                mid = (x_i + x_j, y_i + y_j)  
                smap = mid_map.get(mid)
                if smap is None:
                    mid_map[mid] = {slope: 1}
                else:
                    smap[slope] = smap.get(slope, 0) + 1
        
        total_parallel_segment_pairs = 0
        for slope, cmap in slope_map.items():
            S = sum(cmap.values())
            if S < 2:
                continue
            total_pairs = S*(S-1)//2
            same_line_pairs = 0
            for cnt in cmap.values():
                if cnt > 1:
                    same_line_pairs += cnt*(cnt-1)//2
            total_parallel_segment_pairs += (total_pairs - same_line_pairs)
        
        total_parallelograms = 0
        for mid, smap in mid_map.items():
            T = sum(smap.values())
            if T < 2:
                continue
            total_pairs = T*(T-1)//2
            same_slope_pairs = 0
            for cnt in smap.values():
                if cnt > 1:
                    same_slope_pairs += cnt*(cnt-1)//2
            total_parallelograms += (total_pairs - same_slope_pairs)
        
        return total_parallel_segment_pairs - total_parallelograms