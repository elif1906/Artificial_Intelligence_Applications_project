from ..Parameters import Node, Queue

class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.number_of_explored_nodes = 0
        self.explored_nodes = set()
        
        self.queue = Queue()
        start = Node(self.maze.start, None, None)
        self.queue.push(start)
        
        return
    
    def solve(self):
        while True:
            if self.queue.is_empty():
                raise Exception("Maze is invalid. No solution exists.")
            
            node = self.queue.pop()
            self.number_of_explored_nodes += 1
            
            if node.state == self.maze.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                
                solution = (actions[::-1], cells[::-1])
                self.maze.set_solution(solution)
                return
                
            self.explored_nodes.add(node.state)
            
            for action, state in self.maze.get_available_actions(node.state):
                if (not self.queue.does_contain_state(state)) and (state not in self.explored_nodes):
                    child = Node(state, node, action)
                    self.queue.push(child)
                    
        return
    