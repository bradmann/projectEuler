import sys

routeCount = 0
grid = []

def findPaths(position, maxRight, maxDown):
    if position[0] == maxRight and position[1] == maxDown:
        global routeCount
        routeCount += 1
        
    if position[0] < maxRight:
        findPaths([position[0] + 1, position[1]], maxRight, maxDown)

    if position[1] < maxDown:
        findPaths([position[0], position[1] + 1], maxRight, maxDown)

    
def computeRoutes(position):
    global grid
    
    if position[0] == 0 and position[1] == 0:
        return 2

    if position[0] == 0:
        return grid[position[0]][position[1] - 1] + 1

    if position[1] == 0:
        return grid[position[0] - 1][position[1]] + 1

    return grid[position[0] - 1][position[1]] + grid[position[0]][position[1] - 1]

if __name__ == "__main__":
    gridNum = int(20)

    for x in range(gridNum):
        grid.append([])
        for y in range(gridNum):
            grid[x].append(computeRoutes([x, y]))
    
    print(grid[gridNum-1][gridNum-1])
