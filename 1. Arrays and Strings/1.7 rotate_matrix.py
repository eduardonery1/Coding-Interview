from random import randint

def grid(n=3, m=3):
    return [[randint(1, 10) for item in range(m)] for row in range(n)]

def grid_printer(g):
    for row in g:
        print(row, "\n")
    print("#"*30)

def rotate_matrix(grid):
    n = len(grid) 
    new_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[n - j - 1][i] = grid[i][j]
    return new_matrix

def change_values(grid, i, j, N):
    adresses = [(i, j)]
    values = []
    for idx in range(4):
        i = adresses[idx][0]
        j = adresses[idx][1]
        values.append(grid[i][j])
        adresses.append((N - j - 1, i))
        #print(i, j)
    for idx in range(4):
        if idx == 3: 
            i = adresses[0][0]
            j = adresses[0][1]
        else:
            i = adresses[idx+1][0]
            j = adresses[idx+1][1]
        grid[i][j] = values[idx]
    #print("fim ciclo\n")

def change_grid(grid, start, end, N):
    if start >= end: return 
    for idx_col in range(start, end):
        change_values(grid, start, idx_col, N)
    return change_grid(grid, start+1, end-1, N)

def rotate_matrix_inplace(grid):
    N = len(grid)
    change_grid(grid, 0, N-1, N)
    return grid

if __name__=="__main__":
    test = grid(2, 2)
    grid_printer(test)
    rotate_matrix_inplace(test)
    grid_printer(test)
    grid_printer(rotate_matrix(test))
    assert(rotate_matrix_inplace(test)==rotate_matrix(test))