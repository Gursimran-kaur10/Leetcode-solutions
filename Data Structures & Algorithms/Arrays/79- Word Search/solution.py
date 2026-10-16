class Solution(object):
    def exist(self, board, word):
        rows=len(board)
        cols=len(board[0])

        def dfs(r,c,k):
            if k==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[k]:
                return False
            ch=board[r][c]
            board[r][c]='#'

            found=dfs(r+1,c,k+1)or dfs(r-1,c,k+1)or dfs(r,c+1,k+1) or dfs(r,c-1,k+1)

            board[r][c]=ch
            return found

        for r in range (rows):
            for c in range (cols):
                if dfs(r,c,0):
                    return True
        return False
        
