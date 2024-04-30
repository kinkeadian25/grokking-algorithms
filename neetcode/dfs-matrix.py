def dfs(grid, r, c, visit):
    rows, cols = len(grid),len(grid[0])
    if (min(r, c) < 0 or 
        r == rows or c == cols or
        (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
    
    visit.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))

    return count

grid = [[0,0,0,0],
         [1,1,0,0],
         [0,0,0,1],
         [0,1,0,0]]

print(dfs(grid, 0, 0, set()))