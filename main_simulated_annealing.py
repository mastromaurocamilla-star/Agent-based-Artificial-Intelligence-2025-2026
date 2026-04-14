from local_search.simulated_annealing import SimulatedAnnealing, Scheduler
from problems.chessQueens.chessQueens import ChessQueensProblem
import random

if __name__ == "__main__":
    problem = ChessQueensProblem(8)
    random.seed = 42
    scheduler = Scheduler(iterations=10000, alpha=0.01, scheduler='exponential')
    search = SimulatedAnnealing(problem, scheduler=scheduler)
    result = search.search()
    score = problem.evaluate(result)
    print(f'Solution score: {score}')
    problem.print_state(result)