def twod(bombs:list=[], rows: int=0, cols: int=0) -> list:
    grid = [[0 for col in range(cols)]for row in range(rows)]
    for bomb in bombs:
        grid[bomb[0]][bomb[1]] = -1
        (row_i, col_i) = bomb
        for i in range(row_i -1, row_i+2):
            for j in range(col_i-1, col_i+2):
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] != -1:
                    grid[i][j] += 1
    return grid

grid1 = twod(bombs=[[0, 0], [0, 1]], rows=3, cols=4)

def click(grid, rows, cols, given_row, given_col):
    from collections import deque
    neigh = deque([])
    if grid[given_row][given_col] == 0:
        neigh.append((given_row, given_col))
    while neigh:
        (row_i, col_i) = neigh.popleft()
        grid[row_i][col_i] = -2
        for i in range(row_i - 1, row_i + 2):
            for j in range(col_i - 1, col_i + 2):
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 0:
                    neigh.append([i, j])
    return grid

field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

print(click(grid1, 3, 4, 0, 3))
print(click(field2, 4, 4, 0, 3))
        
        

