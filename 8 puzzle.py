from collections import deque

print("Enter Initial State:")
start = tuple(tuple(map(int, input().split())) for _ in range(3))

print("Enter Goal State:")
goal = tuple(tuple(map(int, input().split())) for _ in range(3))

# Generate next possible states
def get_moves(state):
    state = [list(row) for row in state] # converts the tuple to list 

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    moves = [] #stors the new puzzle state 

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:  #checks for new position
            temp = [row[:] for row in state]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y] 
            moves.append(tuple(tuple(r) for r in temp)) #back to tuple 

    return moves

# BFS
queue = deque([(start, [start])])
visited = set()

while queue:
    state, path = queue.popleft() #empty    

    if state == goal:
        print("\nGoal Reached!")
        print("Moves =", len(path) - 1)

        for i, board in enumerate(path): #loops through every puzzle state 
            print("\nStep", i)
            for row in board:
                print(row)
        break

    if state not in visited:
        visited.add(state)   #makes the current state as visited 
 
        for move in get_moves(state):
            if move not in visited:
                queue.append((move, path + [move]))
else:
    print("No Solution Found")
