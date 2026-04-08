class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create dictionary with 9 * 3 keys storing 
        # all the seen values of that row / column / block
        seen = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                block = (i // 3, j // 3)
                if num == ".":
                    continue
                if (num in seen[f'row{i}'] or
                    num in seen[f'col{j}'] or
                    num in seen[f'block{block}']):
                    return False
                seen[f'row{i}'].add(num)
                seen[f'col{j}'].add(num)
                seen[f'block{block}'].add(num)
        return True


