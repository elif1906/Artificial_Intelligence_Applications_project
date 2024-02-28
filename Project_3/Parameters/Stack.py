from .Queue import Queue

class Stack(Queue):
    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop Node object: Stack frontier is empty!")
        
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
    