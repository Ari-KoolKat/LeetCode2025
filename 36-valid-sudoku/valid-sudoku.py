class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hr={i:[] for i in range(9)}
        hc={j:[] for j in range(9)}
        hb={k:[] for k in range(9)}
        r=len(board)
        c=len(board[0])
        for i in range(r):
            for j in range(c):
                p=board[i][j]
                if p=='.':
                    continue
                if p not in hr[i]:
                    hr[i].append(p)
                else:
                    return False
                if p not in hc[j]:
                    hc[j].append(p)
                else:
                    return False
                bi=(i//3)*3+(j//3)
                if p not in hb[bi]:
                    hb[bi].append(p)
                else:
                    return False
        return True