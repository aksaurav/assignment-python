# Python


def max_moves(grid):
    m, n = len(grid), len(grid[0])
    moves = [[0] * n for _ in range(m)]  # Intialize the all the moves with 0's

    # set the directions
    directions = [(-1, 1), (0, 1), (1, 1)]

    max_moves = 0  # keep track of the max moves

    for i in range(m):
        # Enqueue
        queue = [(i, 0, 1)]
        visited = set()

        while queue:
            row, col, move = queue.pop(0)
            visited.add((row, col))

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and (new_row, new_col) not in visited
                    and grid[new_row][new_col] > grid[row][col]
                ):
                    moves[new_row][new_col] = max(moves[new_row][new_col], move)
                    max_moves = max(max_moves, moves[new_row][new_col])
                    queue.append((new_row, new_col, move + 1))

    return max_moves


grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
result = max_moves(grid)
print(result)  # output = 3

grid = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
result = max_moves(grid)
print(result)  # output = 0

"""                     My Thought Process                  """


"""
Problem Statement (in my words): Given a matrix starting from index value 0, which is `mxn` grid also containing all 
positive numbers. We can go to the next cell (row,col) only if the next (row, col) is strictly greater than the current (row,col)

We have to return the maximun number of moves (top-bottom, left-right) (indicating a BFS solutions in my mind) that we can perform.


Example inputs and outputs:

Example 1:
input: grid = [
    [2,4,3,5],
    [5,4,9,3],
    [3,4,2,11],
    [10,9,13,15]
    ]
output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
    - (0, 0) -> (0, 1), we can go from (0, 0) to (0, 1) b/c its a greater value. (moveCount = 1)
    - (0, 1) -> (1, 2), from (0, 1) we can go to (1, 2) b/c its a greater value. (moveCount = 2)
    - (1, 2) -> (2, 3), from (1, 2) we can go to (2, 3) b/c its a greater value. (moveCount = 3)
It can be shown that it is the maximum number of moves that can be made.

Example 2: 
input: grid = [
    [3,2,4],
    [2,1,9],
    [1,1,7]
    ]

output: 0
Explanation: We can start at the cell (0, 0) and make the following moves
    - (0, 0) -> (0, 1), We cannot go from (0, 0) to (0, 1) b/c its a less value than. (moveCount = 0)
    - (0, 0) -> (1, 1), We cannot go from (0, 0) to (1, 1) b/c its a less value than. (moveCount = 0)


    
-> Brute Force: 
    - Lets just go through every single row,col in our grid
    - Try some kind traversal with nested loops 
    - perform the operation from every single cells
    - Return the maximun moves 
Time Complexity --> O(n^2), where n is the number of nodes in the grid/graph. We will visiting every single value twich


-> Optimizations --> BFS (can do with DFS as well, but I like BFS better)
    - 1st we will get the dimensions of the grid 
    - maintain a move count variable to count every moves 
    - Use a hash set track the visited set and not to visit the same value twice 
    - Choose the 1st (0, 0) cell as a starting point
    - Initilize the move variable
    - initialize a Queue and append the current row,col
    - While we have values in our Queue:
        - go to next row, col 
        - if we are still in bounds and 
        - if the (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1) --> (top and bottom, left and right)
        - is strictly greater than the current row, col 
        - If we can go to next row,col --> update the move count by one
        - Append the row,col into the Queue
    - Update MaxMove with the move count
-> Time Complexity --> O(n), Worst case is where every next node/value is greater than the current node/value,
    we have to visit every single node only ONCE

"""
