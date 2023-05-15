from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        queue = deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            curr_row, curr_col, steps = queue.popleft()

            for direction in directions:
                next_row = curr_row + direction[0]
                next_col = curr_col + direction[1]

                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == ".":

                    if 0 == next_row or next_row == rows -1 or 0 == next_col or next_col == cols -1:
                        return steps +1
                
                    maze[next_row][next_col] = '+'
                    queue.append([next_row, next_col, steps + 1])

        return -1
    
        