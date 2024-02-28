import sys
from Project_3.Parameters import Maze
from Project_3.search import BFS, DFS , A_search


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <maze_file>")
        return 1

    m = Maze(sys.argv[1])
    print("Maze:")
    m.print_maze()
    m.output_image("maze.png", show_explored=True)
    
    
     # Solve with BFS
    print("Solving with BFS:")
    bfs = BFS(m)
    bfs.solve()
    print("Number of explored nodes (BFS):", bfs.number_of_explored_nodes)
    
    print("Solution after BFS:")
    m.print_maze()
    
    

    # Solve with DFS
    print("\nSolving with DFS:")
    dfs = DFS(m)
    dfs.solve()
    print("Number of explored nodes (DFS):", dfs.number_of_explored_nodes)
    
    print("Solution after DFS:")
    m.print_maze()
    
  
    # Solve with A * search
   
    print("\nSolving with A* search:")
    a_star = A_search(m)
    a_star.solve()
    print("Number of explored nodes (A* search):", a_star.number_of_explored_nodes)
    print("Solution after A* search:")
    m.print_maze()
    
    return 0

if __name__ == '__main__':
    main()
