class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        R=len(heights) #Number of Rows
        C=len(heights[0]) #number of Coloumns
        p=set() #set for visited for pacific
        a=set() #set for the visited for Atlantic
        def dfs(r,c,visit,prevh): #here visit will be the ocean we checking 
            if (r,c) in visit or r<0 or c<0 or r==R or c==C or heights[r][c]<prevh:
                return  #if this node already visited or not match the pattern
            visit.add((r,c)) #adding as visited
            dfs(r+1,c,visit,heights[r][c]) #checking bottom
            dfs(r-1,c,visit,heights[r][c]) #checking upper
            dfs(r,c+1,visit,heights[r][c]) #check left one
            dfs(r,c-1,visit,heights[r][c]) #check right one
        for c in range(C): #this will check for each coloumn from that row and those adjacent
            dfs(0,c,p,heights[0][c]) #checking from top row as it touches Pacific
            dfs(R-1,c,a,heights[R-1][c]) #bottom row as it touches Atlantic
        for r in range(R): #similarly but here we check left and right coloumn
            dfs(r,0,p,heights[r][0]) #left coloumn as it touches Pacific
            dfs(r,C-1,a,heights[r][C-1]) #right coloumn As it touches atlantic
        res=[] #our common cells
        for r in range(R): #traverse entire matrix
            for c in range(C):
                if (r,c) in p and (r,c) in a: #if cell can be reached by both
                    res.append((r,c)) #add to result
        return res #returning the result