############################### Graph Traversal (General) ###############################
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect:
# - A cell is connected to adjacent cells horizontally or vertically.
# Region:
# - To form a region connect every 'O' cell.
# Surround:
# - The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]


# xxxx      xxxx
# xoox      xxxx
# xxox  =>  xxxx
# xoxx      xoxx
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.


# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]
#############################################################



#-------------- SOLUTION 01 BFS ----------------------#
# Time complexity : O(MXN)
# Space complexity : O(MXN) in worse case

# First, check the four border of the matrix. If there is a element is
# 'O', alter it and all its neighbor 'O' elements to 'N'.

# Then ,alter all the 'O' to 'X'
# At last,alter all the 'N' to 'O'

# example:
# X X X X           X X X X             X X X X
# X X O X  ->       X X O X    ->       X X X X
# X O X X           X N X X             X O X X
# X O X X           X N X X             X O X X
#-----------------------------------------------------#
from collections import deque

class SolutionBFS:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return

        # queue for bfs
        q = deque()
        # start from the boarder and replace all O to N
        # put all the boarder value into queue.
        for r in range(R):
            q.append((r, 0))
            q.append((r, C-1))

        for c in range(C):
            q.append((0, c))
            q.append((R-1, c))

        while q:
            r, c = q.popleft()
            if 0<=r<R and 0<=c<C and board[r][c] == "O":
                # modify the value from O to N
                board[r][c] = "N"
                # append the surrouding cells to queue.
                q.append((r, c+1))
                q.append((r, c-1))
                q.append((r-1, c))
                q.append((r+1, c))

        # replace all the O to X, then replace all the N to O
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"

solutionBFS = SolutionBFS()
solutionBFS.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
solutionBFS.solve([["X"]])
print("------------------------")



#-------------- SOLUTION 01 DFS ----------------------#
# recursion, dfs
#-----------------------------------------------------#
class SolutionDFS:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return

        # start from the boarder and replace all O to N
        # put all the boarder value into queue.
        for r in range(R):
            self.dfs(board, r, 0, R, C)
            self.dfs(board, r, C-1, R, C)

        for c in range(C):
            self.dfs(board, 0, c, R, C)
            self.dfs(board, R-1, c, R, C)

        # replace all the O to X, then replace all the N to O
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"

    def dfs(self, board, r, c, R, C):
        if 0<=r<R and 0<=c<C and board[r][c] == "O":
            board[r][c] = "N"
            self.dfs(board, r, c+1, R, C)
            self.dfs(board, r, c-1, R, C)
            self.dfs(board, r-1, c, R, C)
            self.dfs(board, r+1, c, R, C)


solutionDFS = SolutionDFS()
solutionDFS.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
solutionDFS.solve([["X"]])
print("------------------------")


#------------- SOLUTION 02 -----------------#
# Start from the boundary, and use DFS (or BFS) to flip the 'O's that are connected to the edge to a third symbol (e.g., "Z")
# Scan the matrix again to flip the remaining 'O' to 'X', and the third symbol back to 'O'
#---------------------------------------------#

class Solution_02:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
            board[row][col] = "Z"
            for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1):
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] != 'O':
                    continue
                dfs(nr, nc)

        def flip():
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == "Z":
                        board[row][col] = "O"
                    elif board[row][col] == "O":
                        board[row][col] = "X"

        for row in [0, rows - 1]:
            for col in range(cols):
                if board[row][col] == 'O':
                    dfs(row, col)

        for col in [0, cols - 1]:
            for row in range(1, rows - 1):
                if board[row][col] == 'O':
                    dfs(row, col)

        flip()


solution02 = Solution_02()
solution02.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
solution02.solve([["X"]])
print("------------------------")





#----------------- SOLUTION 03 ------------------------#
#------------------------------------------------------#

class Solution_03:
    def solve(self, board):
        if not any(board): return

        m, n = len(board), len(board[0])
        edge_cordinates = []

        for k in range(max(m, n)):
            edges = (0, k), (m-1, k), (k, 0), (k, n-1)
            for edge in (edges):
                if edge not in edge_cordinates and edge[0] < m and edge[1] < n:
                    edge_cordinates.append(edge)


        while edge_cordinates:
            i, j = edge_cordinates.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "S"
                edge_cordinates += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board


def solve(self, board):
    if not any(board): return

    m, n = len(board), len(board[0])
    save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
    while save:
        i, j = save.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'S'
            save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

    for row in board:
        for i, c in enumerate(row):
            row[i] = 'XO'[c == 'S']


solution03 = Solution_03()
solution03.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
solution03.solve([["X"]])
print("------------------------")




#--------------- SOLUTION 04 ---------------------#
#-------------------------------------------------#
class Solution_04:
    def dfs(self, vis, board, sr, sc, n, m):
        # Base condition to stop the DFS
        if sr < 0 or sr >= n or sc < 0 or sc >= m or vis[sr][sc] == 1 or board[sr][sc] != 'O':
            return

        # Mark the current cell as visited
        vis[sr][sc] = 1

        # Recursively call DFS for the four adjacent cells
        self.dfs(vis, board, sr - 1, sc, n, m)  # Up
        self.dfs(vis, board, sr + 1, sc, n, m)  # Down
        self.dfs(vis, board, sr, sc - 1, n, m)  # Left
        self.dfs(vis, board, sr, sc + 1, n, m)  # Right

    def solve(self, board):
        if not board:  # Edge case: empty board
            return

        n = len(board)
        m = len(board[0])

        # Create a visited matrix initialized to 0
        vis = [[0 for _ in range(m)] for _ in range(n)]

        # Perform DFS from the 'O's on the borders
        for i in range(m):
            if board[0][i] == 'O':
                self.dfs(vis, board, 0, i, n, m)
            if board[n - 1][i] == 'O':
                self.dfs(vis, board, n - 1, i, n, m)

        for i in range(n):
            if board[i][0] == 'O':
                self.dfs(vis, board, i, 0, n, m)
            if board[i][m - 1] == 'O':
                self.dfs(vis, board, i, m - 1, n, m)

        # Update the board: Convert all 'O's not visited by DFS to 'X'
        for i in range(n):
            for j in range(m):
                if vis[i][j] != 1 and board[i][j] == 'O':
                    board[i][j] = 'X'


solution04 = Solution_04()
solution04.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
solution04.solve([["X"]])
print("------------------------")
