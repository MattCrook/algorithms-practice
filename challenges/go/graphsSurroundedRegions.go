//############################### Graph Traversal (General) ###############################//
// You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

// Connect:
// - A cell is connected to adjacent cells horizontally or vertically.
// Region:
// - To form a region connect every 'O' cell.
// Surround:
// - The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
// A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

// Example 1:
// Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
// Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

// xxxx      xxxx
// xoox      xxxx
// xxox  =>  xxxx
// xoxx      xoxx
// In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

// Example 2:
// Input: board = [["X"]]
// Output: [["X"]]
//#############################################################//

// ----------------Solution 01 ---------//
// This problem could be solved two ways:

// Identify all isolated 'O' cells and mark them as 'X' then.
// Mark all accessible from boarders 'O' and then turn all inaccessible ones into 'X'.
// This solution is about the second way.

// To mark cells as "reachable", algorithm changing their values to 'R' instead of 'O'.

// Follow through left and right borders of the board and look for 'O' cells. If found recursevly mark all accessible 'O' cells as 'R'.
// Follow through top and bottom borders of the board and do the same.
// Follow through the whole board and flip 'O' -> 'X' and 'R' -> 'O'
// Time compexity: O(N * M), where N is the height of the board and M is the width of the board. Since in the wrost case algorithm processes all cells twice and O(2 * N * M) == O(N * M)
// Space complexity: O(N * M) — only the fixed set of variables of the fixed size is allocated and all 'marks' are done 'in-place' BUT recursive function calls are stored on the stack and use N * M memory in the worst case. There are no "real" allocations since the stack is allocated when the program starts, but space complexity is about all used space.
// --------------------------------------//
func solve(board [][]byte) {
	n := len(board)
	m := len(board[0])

	// If board have less than 3 size in any direction: nothing to do, because all cells located on borders
	if n < 3 || m < 3 {
		return
	}

	// Go and check left and right borders of the board
	for row := 0; row < n; row++ {
		if board[row][0] == 'O' {
			dfs(row, 0, n, m, board)
		}
		if board[row][m-1] == 'O' {
			dfs(row, m-1, n, m, board)
		}
	}

	// Same for check up and down borders of the board
	// Since corners (0,0) and (n - 1, m - 1) where checked in previous cycle, skip them in this one
	for col := 1; col < m-1; col++ {
		if board[0][col] == 'O' {
			dfs(0, col, n, m, board)
		}
		if board[n-1][col] == 'O' {
			dfs(n-1, col, n, m, board)
		}
	}

	// Follow through the whole board and flip all 'R' cells back into 'O' and all 'O' cell to 'X'
	// since they're unreacheable from the board located 'O' cell if any
	for row := 0; row < n; row++ {
		for col := 0; col < m; col++ {
			if board[row][col] == 'O' {
				board[row][col] = 'X'
			} else if board[row][col] == 'R' {
				board[row][col] = 'O'
			}
		}
	}
}
