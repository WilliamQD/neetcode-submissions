class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(word)
        h = len(board)
        w = len(board[0])

        def search(i, j, idx):
            # 1. Base Case: Found the whole word!
            if idx == n:
                return True
                
            # 2. Out of bounds OR wrong letter OR already visited
            if (i < 0 or i >= h or j < 0 or j >= w or board[i][j] != word[idx]):
                return False

            # 3. Mark as visited (The '# trick')
            temp = board[i][j]
            board[i][j] = "#" 

            # 4. Explore all 4 directions
            # We can chain these with 'or' - if any return True, it stops and returns True!
            found = (search(i-1, j, idx+1) or 
                     search(i+1, j, idx+1) or 
                     search(i, j-1, idx+1) or 
                     search(i, j+1, idx+1))

            # 5. Backtrack: Restore the original letter
            board[i][j] = temp 

            return found

        # Start the DFS from every possible cell
        for i in range(h):
            for j in range(w):
                if search(i, j, 0):
                    return True
                    
        return False