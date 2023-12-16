def heuristic(x):
    value = x
    return value

def hillclimb():
    grid_size = 4
    grid = [
        [1, 2, 3, 4],
        [5, 9, 6, 8],
        [7, 12, 10, 11],
        [13, 14, 15, 16],
    ]

    position = [0, 0]
    maxValue = float('-inf')
    while True:
        oldValue = maxValue
        x = position[0]
        y = position[1]

        possibleMoves = [
            [x - 1, y],
            [x, y - 1],
            [x + 1, y],
            [x, y + 1],
            [x + 1, y + 1],
            [x - 1, y - 1],
            [x + 1, y - 1],
            [x - 1, y + 1]
        ]

        for x1, y1 in possibleMoves:
            if 0 <= x1 < grid_size and 0 <= y1 < grid_size:  
                val = heuristic(grid[x1][y1])

                if val > maxValue:
                    print(f'Better value found: {val}')
                    maxValue = val
                    position = [x1, y1]

        if oldValue == maxValue:
            break
    print(f'The max value of this grid is {maxValue} at position {position}')

hillclimb()
