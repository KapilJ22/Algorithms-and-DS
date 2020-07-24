#AlgoExpert problem: https://www.algoexpert.io/questions/River%20Sizes

def riverSizes(matrix):
    # Write your code here.
    visited = [[False for value in row] for row in matrix]
    result = []

    def dfs(r, c):
        n = len(matrix)
        # print(n)

        if r < 0 or r >= n:
            return 0

        if c < 0 or c >= len(matrix[0]):
            return 0

        if matrix[r][c] == 0 or visited[r][c]:
            return 0
        visited[r][c] = True
        return dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1) + 1

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col]:
                size = dfs(row, col)
                if size > 0:
                    print("here")
                    result.append(size)
                visited[row][col] = True
    return result
