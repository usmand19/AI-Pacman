# AI-Pacman
 Solving Pacman mazes and games using artificial intelligence principles



To play a classic game of pacman with your keyboard, enter the following line into the terminal
<code>python pacman.py
</code>

Run a Depth-First Search (DFS) algorithm on the medium sized maze to find the goal position:
python pacman.py -l mediumMaze  --frameTime=0.05 -p SearchAgent -a fn=dfs

Run a Breadth-First Search (BFS) algorithm on the medium sized maze to find the goal position:
python pacman.py -l mediumMaze --frameTime=0.05 -p SearchAgent -a fn=bfs


Run a Uniform-Cost Search (UCS) algorithm on the medium sized maze to find the goal position:

python pacman.py -l mediumMaze --frameTime=0.05 -p SearchAgent -a fn=ucs


Run a A-Star Search algorithm on a big maze, using a manhattan distance heuristic:
python pacman.py -l bigMaze --frameTime=0.05 -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic



Optimizing a 4-Corners maze using A-Star Search Algorithm:
python pacman.py -l mediumCorners -p SearchAgent -a fn=astar,prob=CornersProblem


Run a classic game of pacman with evaluation function defined in multiAgents.py:
python pacman.py --frameTime 0.1 -p ReflexAgent -k 2 

