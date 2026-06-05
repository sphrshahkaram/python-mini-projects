from collections import deque

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0,0)
goal = (4,4)

queue = deque()
queue.append(start)
visited = set()
came_from = {start: None}
while queue:
    current = queue.popleft()
    visited.add(current)
    if current == goal:
        print("found!!!")
        break

    row , col = current
    neighbors =[
        (row-1 , col),
        (row, col-1),
        (row+1,col),
        (row,col+1)

    ]
    for neighbor in neighbors:

        nrow , ncol = neighbor
        if 0 <= nrow < 5 and 0 <= ncol < 5 and maze[nrow][ncol] == 0 and neighbor not in visited:
            queue.append(neighbor)
            came_from[neighbor] = current
    
        

else: print("no path found!")
path = []
node = goal
while node is not None:
    path.append(node)
    node = came_from[node]
path.reverse()
print(path)
