# AI-Pacman
 Solving Pacman mazes and games using artificial intelligence principles
 
## Description:
The following repository solves varying sizes of Pacman mazes using artificiall intelligence search algorithms, namely Depth-First, Breadth-First, Uniform-Cost, and A-Star Search algorithms. These algorithms are implemented in <code>search.py</code>. In addition, a heuristic function is defined in <code>multiAgents.py</code> that assists Pacman in trying to solve the classic maze with two ghosts present. Below, some lines of code are provided to run the algorithms prior mentioned.

## How To Run:
Copy and paste the line of code provided into a python terminal to run the following:

Play a classic game of Pacman using the keyboard arrows:\
<code>python pacman.py</code>

Run a Depth-First Search (DFS) algorithm on the medium sized maze to find the goal position:\
<code>python pacman.py -l mediumMaze  --frameTime=0.05 -p SearchAgent -a fn=dfs</code>

Run a Breadth-First Search (BFS) algorithm on the medium sized maze to find the goal position:\
<code>python pacman.py -l mediumMaze --frameTime=0.05 -p SearchAgent -a fn=bfs</code>

Run a Uniform-Cost Search (UCS) algorithm on the medium sized maze to find the goal position:\
<code>python pacman.py -l mediumMaze --frameTime=0.05 -p SearchAgent -a fn=ucs</code>

Run a A-Star Search algorithm on a big maze, using a manhattan distance heuristic:\
<code>python pacman.py -l bigMaze --frameTime=0.05 -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic</code>

Optimizing a 4-Corners maze using A-Star Search Algorithm:\
<code>python pacman.py -l mediumCorners -p SearchAgent -a fn=astar,prob=CornersProblem</code>

Run a classic game of pacman with evaluation function defined in multiAgents.py:\
<code>python pacman.py --frameTime 0.1 -p ReflexAgent -k 2</code>



