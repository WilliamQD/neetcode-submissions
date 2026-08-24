class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        h = len(board)
        w = len(board[0])

        def search(idx_path, idx):
            if idx == n:
                # print("reached True")
                return True
            if idx >= n:
                # print("reached Over")
                return 

            i, j = idx_path[-1]
            # Check all 4 directions: (up, down, left, right)
            for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= r < h and 0 <= c < w and board[r][c] == word[idx] and (r, c) not in idx_path:
                    
                    idx_path.append((r, c))
                    # print(f"found {word[idx]} at {(r, c)}")
                    # print(f"idx = {idx}, path={idx_path}")
                    if search(idx_path, idx + 1):
                        return True
                    idx_path.pop()

            # reaching here means no valid direction to go 
            return

        
        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    # start search neighbors
                    if search([(i, j)], 1):
                        return True

        return False