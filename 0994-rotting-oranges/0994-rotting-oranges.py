from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         rotten = collections.deque()
#         number = 0
#         m = len(grid)
#         n = len(grid[0])
#         minute = 0
        
#         for row in range(m):
#             for col in range(n):
#                 if grid[row][col] == 2:
#                     rotten.append((row,col))
#                 elif grid[row][col] == 1:
#                     number += 1
        
#         #special cases
#         if number == 0:
#             return 0
#         if len(rotten) == 0:
#             return -1
        
#         not_in = lambda x , y, arr: (x,y) not in arr
        
#         def checkCoords(left, right, x, y, x_add, y_add):
#             if not_in(x + x_add, y + y_add, visited) and not_in(x + x_add, y + y_add, become_rotten):
#                 if left > right and grid[x + x_add][y + y_add] == 1:
#                     grid[x + x_add][y + y_add] = 2
#                     become_rotten.append((x+x_add, y+y_add))
#                     return -1
#             return 0
#         #bfs on all rottens
#         #add all rottens to a queue
#         queue = collections.deque([rotten])
#         # print('queue', queue)
#         #already rotten oranges that have been checked
#         visited = []
#         #go through each rotten and append if any oranges adjacent
#         while queue and number > 0:
#             #curr iteration - list of rottens
#             curr_rotten = queue.popleft()
#             become_rotten = collections.deque()
#             # print('visited', visited)
#             # print('current rotten', curr_rotten)
#             # print('number', number)
#             while curr_rotten:
#                 #what will become rotten
#                 #current rotten orange
#                 orange = curr_rotten.popleft()
#                 visited.append(orange)
#                 x, y = orange
#                 number += checkCoords(x, 0,x, y, -1, 0)
#                 number += checkCoords(m-1, x, x, y, 1, 0)
#                 number += checkCoords(y, 0, x, y, 0, -1)
#                 number += checkCoords(n-1, y,x, y, 0, 1)
#             if become_rotten:
#                 queue.append(become_rotten)
#             minute += 1
#         return -1 if number > 0 else minute
                    
                    
                    
                    