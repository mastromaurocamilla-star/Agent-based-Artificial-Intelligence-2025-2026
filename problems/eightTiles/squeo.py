class EightTilesProblem:
    def __init__(self, initial_state, goal_state, divsize):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self._divsize = divsize #Dimensione del lato del quadrato, ad esempio 3 per un 3x3

    def actions(self, state):
        possible_actions = []
        zero_x, zero_y = self.find_zero(state)
        if zero_x > 0:
            possible_actions.append('up')
        if zero_x < self._divsize - 1:
            possible_actions.append('down')
        if zero_y > 0:
            possible_actions.append('left')
        if zero_y < self._divsize - 1:
            possible_actions.append('right')
        return possible_actions


    def result(self, state, action):
        zero_x, zero_y = self.find_zero(state)
        if action == 'up':
            new_x, new_y = zero_x - 1, zero_y
        elif action == 'down':
            new_x, new_y = zero_x + 1, zero_y
        elif action == 'left':
            new_x, new_y = zero_x, zero_y - 1
        elif action == 'right':
            new_x, new_y = zero_x, zero_y + 1

        new_state = list(state)
        new_state[zero_x*self._divsize + zero_y], new_state[new_x*self._divsize + new_y] = new_state[new_x*self._divsize + new_y], new_state[zero_x*self._divsize + zero_y]
        return tuple(new_state)


    def is_goal(self, state):
        return state == self.goal_state

    def manhattan_distance(self, state, goal_state):
        distance = 0
        for i in range(len(state)):
            value = state[i]
            current_x, current_y = divmod(i, self._divsize)
            goal_x, goal_y = divmod(goal_state.index(value), self._divsize)
            distance += abs(current_x - goal_x) + abs(current_y - goal_y)
        return distance

    def find_zero(self, state):
        for i in range(len(state)):
            if state[i] == 0:
                return i//self._divsize, i%self._divsize

    def action_cost(self, state, action):
        return 1
    
    def heuristic(self, state):
        return self.manhattan_distance(state, self.goal_state)