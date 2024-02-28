from ..Parameters import Node, Queue

class A_search:
    def __init__(self, maze):
        self.maze = maze
        self.number_of_explored_nodes = 0
        self.explored_nodes = set()
        
        self.queue = Queue()
        start = (Node(self.maze.start, None, None), 0)
        self.queue.push(start)
        
        return
    
    def g_n(self, cost):
        return cost + 1
    
    def h_n(self, state):
        goal_row, goal_column = self.maze.goal
        row, column = state
        return abs(goal_row - row) + abs(goal_column - column)
    
    def gn_plus_hn(self, node_with_cost):
        node, cost = node_with_cost
        return (self.g_n(cost) + self.h_n(node.state))
    
    def solve(self):
        while True:
            if self.queue.is_empty():
                raise Exception("Maze is invalid. No solution exists.")
        
            self.queue.frontier.sort(key = self.gn_plus_hn)
            current_node, current_cost = self.queue.pop()
            self.number_of_explored_nodes += 1
        
            if current_node.state == self.maze.goal:
                actions = []
                cells = []
                while current_node.parent is not None:
                    actions.append(current_node.action)
                    cells.append(current_node.state)
                    current_node = current_node.parent
                
                solution = (actions[::-1], cells[::-1])
                self.maze.set_solution(solution)
                return
        
            self.explored_nodes.add(current_node.state)
            
            for action, state in self.maze.get_available_actions(current_node.state):
                if (not self.queue.does_contain_state_check_for_astar(state)) and (state not in self.explored_nodes):
                    cost = self.g_n(current_cost)
                    child_node = Node(state, current_node, action)
                    child = (child_node, cost)
                    self.queue.push(child)
                
        return