"""
You’ve been asked to simulate a laser security system in a museum vault.
The room is represented as a 2D grid of characters, where:
'E' = empty cell
'L' = a laser (fires in four directions unless blocked)
'W' = wall (blocks laser beams)
'T' = target (needs to be checked whether it gets hit by a laser)

!! Your task is to return a list of coordinates for all targets that get hit by at least one laser beam.

Rules:
Lasers fire up/down/left/right
Beams stop when they hit a wall 'W'
Targets can be hit by multiple lasers
Return target positions as a list of (row, col) tuples

Sample input grid:
grid = [
    ['E', 'L', 'E', 'E', 'T'],
    ['W', 'W', 'E', 'W', 'E'],
    ['E', 'E', 'T', 'E', 'E'],
    ['E', 'L', 'E', 'W', 'T'],
]

"""