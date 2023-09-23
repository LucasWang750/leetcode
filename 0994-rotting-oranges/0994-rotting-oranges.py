class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = collections.deque()
        number = 0
        m = len(grid)
        n = len(grid[0])
        minute = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rotten.append((row,col))
                elif grid[row][col] == 1:
                    number += 1
        
        #special cases
        if number == 0:
            return 0
        if len(rotten) == 0:
            return -1
        
        not_in = lambda x , y, arr: (x,y) not in arr
        
        def checkCoords(left, right, x, y, x_add, y_add):
            if not_in(x + x_add, y + y_add, visited) and not_in(x + x_add, y + y_add, become_rotten):
                if left > right and grid[x + x_add][y + y_add] == 1:
                    grid[x + x_add][y + y_add] = 2
                    become_rotten.append((x+x_add, y+y_add))
                    return -1
            return 0
        #bfs on all rottens
        #add all rottens to a queue
        queue = collections.deque([rotten])
        # print('queue', queue)
        #already rotten oranges that have been checked
        visited = []
        #go through each rotten and append if any oranges adjacent
        while queue and number > 0:
            #curr iteration - list of rottens
            curr_rotten = queue.popleft()
            become_rotten = collections.deque()
            # print('visited', visited)
            # print('current rotten', curr_rotten)
            # print('number', number)
            while curr_rotten:
                #what will become rotten
                #current rotten orange
                orange = curr_rotten.popleft()
                visited.append(orange)
                x, y = orange
                number += checkCoords(x, 0,x, y, -1, 0)
                number += checkCoords(m-1, x, x, y, 1, 0)
                number += checkCoords(y, 0, x, y, 0, -1)
                number += checkCoords(n-1, y,x, y, 0, 1)
            if become_rotten:
                queue.append(become_rotten)
            minute += 1
        return -1 if number > 0 else minute
                    
                    
                    
                    