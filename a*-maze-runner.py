import heapq

maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

frontier = []
heapq.heappush(frontier, (0, start))

came_from = {start: None}
g_score = {start: 0}
visited = set()

while frontier:
    f, current = heapq.heappop(frontier)
    
    if current == goal:
        print("found!!!")
        break
    
    visited.add(current)
    
    row, col = current
    neighbors = [
        (row-1, col),
        (row, col-1),
        (row+1, col),
        (row, col+1)
    ]
    
    for neighbor in neighbors:
        nrow, ncol = neighbor
        if 0 <= nrow < 5 and 0 <= ncol < 5 and maze[nrow][ncol] == 0 and neighbor not in visited:
            g = g_score[current] + 1
            h = heuristic(neighbor, goal)
            f = g + h
            if neighbor not in g_score or g < g_score[neighbor]:
                g_score[neighbor] = g
                came_from[neighbor] = current
                heapq.heappush(frontier, (f, neighbor))
else:
    print("no path found!")

path = []
node = goal
while node is not None:
    path.append(node)
    node = came_from[node]
path.reverse()
print(path)
