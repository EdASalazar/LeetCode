class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))

        for row in range(n -1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                # print('rc', row, column, cells[label])
                label += 1
            columns.reverse()
        dist = [-1] * (n * n + 1)
        # # print('dist', dist)
        q = deque([1])
        dist[1] = 0

        while q:
            # print('1', q)
            curr = q.popleft()
           
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next]
        
                # print('next', next, row, column)
                destination = (board[row][column] if board[row][column] != -1 else next)
                # print('a', q)
                # print("destination",destination)
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
                    # print('2', q)
        return dist[n * n]