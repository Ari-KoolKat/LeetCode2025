class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]  
        cols = [set() for _ in range(9)]   
        boxes = [set() for _ in range(9)]  
        empties = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    b = (r // 3) * 3 + (c // 3) 
                    boxes[b].add(val)
        def backtrack():
            if not empties:
                return True
            best_cell = None
            best_candidates = None
            for (r, c) in empties:
                b = (r // 3) * 3 + (c // 3)
                used_digits = rows[r] | cols[c] | boxes[b]
                candidates = set("123456789") - used_digits
                if best_candidates is None or len(candidates) < len(best_candidates):
                    best_candidates = candidates
                    best_cell = (r, c)
            r, c = best_cell
            b = (r // 3) * 3 + (c // 3)
            empties.remove((r, c))
            for digit in best_candidates:
                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[b].add(digit)
                if backtrack():
                    return True
                board[r][c] = "."
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[b].remove(digit)
            empties.append((r, c)) 
            return False
        backtrack()