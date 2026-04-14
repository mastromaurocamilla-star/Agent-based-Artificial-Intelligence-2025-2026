from problems.eightTiles.polieri import *
from path_search.search import Search
from path_search.strategies import BreadthFirstStrategy

goal_state = (
   (1, 2, 3),
   (4, 5, 6),
   (7, 8, 0)
)

initial_state = (
    (0, 1, 3),
    (4, 2, 5),
    (7, 8, 6)
)

prb = Problem(initial_state, goal_state)

search = Search(prb, BreadthFirstStrategy())

result = search.run()

if result is None:
    print('No solution found')
else:
    print(result)
    print(result.state)
    print(result.path_cost)
    print(result.path())
