from problems.eightTiles.squeo import EightTilesProblem
from path_search.strategies import *
from path_search.search import Search

### Versione semplificata
#goal_state = (2,7,5,0,1,3,4,6,8)
#initial_state = (5, 2, 7, 0, 1, 3, 4, 6, 8)

### Traccia puzzle
#goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
#initial_state = (5, 2, 7, 8, 4, 0, 1, 3, 6)

### Attuale puzzle
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
initial_state = (3, 5, 6, 1, 2, 7, 8, 0, 4)

divsize = 3

prob = EightTilesProblem(initial_state, goal_state, divsize)
strategy = AStarStrategy(prob)
search = Search(prob, strategy)
solution = search.run()

if solution is None:
    print('No solution found')
else:
    print(solution)
    print(solution.state)
    print(solution.path_cost)
    print(solution.path())

if solution is not None:
    path = solution.path()
    state = prob.initial_state
    for action in path:
        print(f'[{state}] --{action}--> ', end='')
        state = prob.result(state, action)
    print(f'[{state}]')
    print(f'Path cost: {solution.path_cost}')