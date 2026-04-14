from local_search.hill_climbing import HillClimbing
from problems.chessQueens.chessQueens import ChessQueensProblem
import random

if __name__ == "__main__":

    runs = 10
    best_solution = None
    # very low score
    best_score = -1000000
    accepted_score = 0
    problem = ChessQueensProblem(8)

    for run in range(runs):
        random.seed = 42+run
        problem.initial_state = problem.random_state()
        print(f"Run {run} over {runs}")
        search = HillClimbing(problem)
        result = search.search()
        score = problem.evaluate(result)
        if score > best_score:
            best_solution = result
            best_score = score
        if score >= accepted_score:
            break
        
    print(f'Best solution score: {best_score}')
    problem.print_state(best_solution)