# Author: Polieri Francesco
# Date: 2026-04-11

# p = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 0]
# ]

# MOVE_UP: sposta lo 0 in alto -> scambio i valori della cella in alto con quella in basso(che è la 0)
# MOVE_DOWN: sposta lo 0 in BASSO -> scambio i valori della cella in basso con quella in alto(che è la 0)
# MOVE_LEFT: sposta lo 0 a SX -> scambio i valori della cella a SX con quella a DX(che è la 0)
# MOVE_RIGHT: sposta lo 0 a DX -> scambio i valori della cella a DX con quella a SX(che è la 0)

MOVE_UP = "MOVE_UP"
MOVE_DOWN = "MOVE_DOWN"
MOVE_LEFT = "MOVE_LEFT"
MOVE_RIGHT = "MOVE_RIGHT"



def trova_zero(matrix):
    # enumerate restituisce l'indice della riga i e tutta la riga stessa
    for i, riga in enumerate(matrix):
        # scopone la riga corrente estraendo l'indice della colonna j
        # e il valore dell'elemento in i, j
        for j, valore in enumerate(riga):
            if valore == 0:
                return i, j
    return None

class Problem:

    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        row, col = trova_zero(state)
        actions = []

        if row != 0:
            actions.append(MOVE_UP)
        if row != 2:
            actions.append(MOVE_DOWN)
        if col != 2:
            actions.append(MOVE_RIGHT)
        if col != 0:
            actions.append(MOVE_LEFT)
        return actions

    def result(self, state, action):
        row, col = trova_zero(state)

        # ogni r è una riga della matrice
        # per ogni riga viene creata una lista
        # creo una copia di new_state
        new_state = [list(r) for r in state]

        if action == MOVE_UP:
            new_state[row][col] = new_state[row-1][col]
            new_state[row-1][col] = 0
        if action == MOVE_DOWN:
            new_state[row][col] = new_state[row+1][col]
            new_state[row+1][col] = 0
        if action == MOVE_LEFT:
            new_state[row][col] = new_state[row][col-1]
            new_state[row][col-1] = 0
        if action == MOVE_RIGHT:
            new_state[row][col] = new_state[row][col+1]
            new_state[row][col+1] = 0

        new_state = tuple(tuple(row) for row in new_state)

        return new_state

    def is_goal(self, state):
        if state == self.goal_state:
            return True
        
    def action_cost(self, state, action):
        return 1