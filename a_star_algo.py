from map_generator import *
import matplotlib.pyplot as plt
from heapq import heappush, heappop

class Solution:
    def __init__(self,IM=None,IN=None, M=None, N=None):
        self.M = M
        self.N = N
        if IN is None and IM is None:
            self.IN = 0
            self.IM = 0
        else:
            self.IN = IN
            self.IM = IM
    def shortestPathBinaryMatrix(self, grid):
        shortest_path = a_star_graph_search(
            start = (self.IM, self.IN), 
            goal_function  = get_goal_function(grid, M=self.M, N=self.N),
            successor_function = get_successor_function(grid), 
            heuristic = get_heuristic(grid, M=self.M, N=self.N)
            )
        if shortest_path is None or grid[0][0] == 1:
            print(-1)
            return -1
        else:
            print(len(shortest_path))
            return shortest_path

def a_star_graph_search(
        start,
        goal_function,
        successor_function,
        heuristic
        ):
    visited = set()
    came_from = dict()
    distance = {start: 0}
    frontier = PriorityQueue()
    frontier.add(start)
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        if goal_function(node):
            return reconstruct_path(came_from, start, node)
        visited.add(node)
        for successor in successor_function(node):
            frontier.add(
                successor,
                priority = distance[node] + 1 + heuristic(successor)
            )
            if (successor not in distance
                or distance[node] + 1 < distance[successor]):
                distance[successor] = distance[node] + 1
                came_from[successor] = node
    return None

def reconstruct_path(came_from, start, end):
    reverse_path = [end]
    while end != start:
        end = came_from[end]
        reverse_path.append(end)
    return list(reversed(reverse_path))

def get_goal_function(grid, M=None,N = None):
    if M is None and N is None:
        M = len(grid)
        N = len(grid[0])
    def is_bottom_right(cell):
        return cell == (M-1, N-1)
    return is_bottom_right

def get_successor_function(grid):
    def get_clear_adjacent_cells(cell):
        i, j = cell
        return (
            (i + a, j + b)
            for a in (-1, 0, 1)
            for b in (-1, 0, 1)
            if a != 0 or b != 0
            if 0 <= i + a < len(grid)
            if 0 <= j + b < len(grid[0])
            if grid[i + a][j + b] == 0
        )
    return get_clear_adjacent_cells

def get_heuristic(grid, M=None,N = None):
    if M is None and N is None:
        M, N = len(grid), len(grid[0])
    (a, b) = goal_cell = (M - 1, N - 1)
    def get_clear_path_distance_from_goal(cell):
        (i, j) = cell
        return max(abs(a - i), abs(b - j))
    return get_clear_path_distance_from_goal

class PriorityQueue:
    
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))
    
    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))
    
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)


grid=[
	[0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0],
	[0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0],
	[1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0],
	[0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1],
	[0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0],
	[1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0],
	[1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1],
	[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
    [1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0],
	[0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1],
	[0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0],
    [0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0],
	[0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0],
	[1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0]
]

grid = get_grid_map()
# print(grid[10][10])
# for i in grid:
#     print(i)

'''
N = y and M = x     for final position
IN = y and IM = x   for initial position
'''
IN = 1
IM = 5
N = 30
M = 35
data = Solution(IN,IM,N,M) 
 
print("start :",grid[IN][IM])
print("End",grid[N][M])

new_data = data.shortestPathBinaryMatrix(grid)
# print(new_data)
for cor in new_data:
    grid[cor[0]][cor[1]] = 0.3

plt.imshow(grid, cmap='gray')
plt.show()