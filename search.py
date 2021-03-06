# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    """
    Search the deepest nodes in the search tree first.

    Returns a list of actions that reaches the
    goal by implementing a graph search algorithm.

    """

    # Declare fringe and action list as Stack data structures, and initialize the fringe with Pacman's starting state
    fringe = util.Stack()
    fringe.push(problem.getStartState())
    action_list = util.Stack()
    action_list.push([])

    # Declare a variable used to check if Pacman is in the goal state or not
    goal_check = problem.getStartState()

    # A variable used to keep track of states Pacman has visited
    master_path = []

    
    # While the frnge is not empty
    while fringe:

		# If the goal state is added to the solution path, we want to break, and store the action used to
        # get to the goal state
        if problem.isGoalState(goal_check):
            actions_path = action_list.pop()
            break
        else:
			# Take the state and action at the top of the fringe and action list
            node = fringe.pop()
            actions_path = action_list.pop()
            # If state is not in master path (Pacman has not explored this state)
            if not (node in master_path):

                # Add it to the list of visited states 
                master_path.append(node) 
                # Get the successors of the current state:
                succ_states = problem.getSuccessors(node)

            for successor in succ_states:

                # If successor state is yet to be explored,  and see if the update the
                if not successor[0] in master_path:
                    
                    # Update the check for the goal state for each successor visited
                    goal_check = successor[0]
                    # Add it to the list of visited states
                    fringe.push(successor[0])
                    # Get the action and state the action moves Pacman into for the successor
                    action_list.push(actions_path + [successor[1]])

    return actions_path

def breadthFirstSearch(problem):

    """Search the shallowest nodes in the search tree first."""

    # Declare fringe and action list as Queue data structures, and initialize the fringe with Pacman's starting state
    fringe = util.Queue()
    fringe.push(problem.getStartState())
    action_fringe = util.Queue()
    action_fringe.push([])

    # A variable used to keep track of states Pacman has visited
    master_path = []

    # While the frnge is not empty
    while fringe:

        # Obtain a state from the top of the fringe, and the list of actions used to get the given state
        node = fringe.pop()
        actions_path = action_fringe.pop()
        # Add the node to the list of places Pacman has travelled to
		# If the goal state/node got added to the solution path, we want to break
        # One major difference from DFS is check if current state is goal, not the successor/previous state
        if problem.isGoalState(node):
            break

        else:

            if not (node in master_path):

                # Add the state to master path 
                master_path.append(node) 
                # Get the successors of the state:
                succ_states = problem.getSuccessors(node)      

            for successor in succ_states:

                # If successor state is yet to be visited by Pacman:
                if not successor[0] in master_path:
                    # Append action and next state pacman moves to for a given successor
                    temp_path = actions_path + [successor[1]]
                    # Push the successor node onto the fringe
                    fringe.push(successor[0])
                    # Update the action list for the given successor
                    action_fringe.push(temp_path)

    return actions_path



def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    # Declare fringe as a Priority Queue data structures, and initialize the fringe with Pacman's starting state
    # as well as a cost of 0
    fringe = util.PriorityQueue()
    start = problem.getStartState()
    fringe.push((start,[]),0)

    # Initialize the check for the goal state with the starting state
    goal_check = start

    # A variable used to keep track of states Pacman has visited
    master_path = []

    # A variable used to keep track of the cost of different states Pacman has visited
    cost_list = []

    # While the frnge is not empty
    while fringe:
		# If the solution got added to the solution path, we want to break
        if problem.isGoalState(goal_check):
            actions_path = action_list
            break
        else:
			# Take the top item of the Priority Queue (lowest cost)
            node, actions_path = fringe.pop()
            
            # If pacman is yet to visit the state
            if not (node in master_path): 
                # Get the successors of the state, and add it to list of visited states:
                master_path.append(node)
                succ_states = problem.getSuccessors(node)

            for successor in succ_states:
                if not successor[0] in master_path:
                    # Add the successor state to the list of states visited
                    goal_check = successor[0]
                    # Get the action and state the action moves Pacman into for the successor
                    action_list = actions_path + [successor[1]]
                    # Use a defined function to get a cost for the given action using a constant heuristc
                    # The cost of a state is the sum of costs of preceding state (each action have acost of 1)
                    ucs_cost = problem.getCostOfActions(action_list)
                    # Append the cost of the successor action to the list of costs for the given action
                    cost_list.append(ucs_cost)
                    # Add the successor to the fringe
                    fringe.push((successor[0],action_list), ucs_cost)
    return actions_path
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    # Declare fringe and action lists as a Priority Queues, and initialize the fringe with Pacman's starting state

    fringe = util.PriorityQueue()
    action_fringe = util.PriorityQueue()
    start = problem.getStartState()
    # The cost of the first node for A* has to be initialized with a functioned because it has to be evaluated
    # for every different maze, a different value might be returned
    fringe.push((start,[]),nullHeuristic(start))
    action_fringe.push([],nullHeuristic(start))

    # Use master_path to keep track of visited states
    master_path = [start[0]]
    # Use action list as a stack to keep track of the different paths
    while fringe:
		# If the goal state got added to the solution path, we want to break
        node, actions_path = fringe.pop()
        if problem.isGoalState(node):
            break
        else:

            if not (node in master_path): 

                # Get the successors of a state:
                succ_states = problem.getSuccessors(node)

            for successor in succ_states:

                if not (successor[0] in master_path): 

                    # Take the front item of the priority que and store action taken to get up to the successor state
                    master_path.append(node)
                    action_list = actions_path + [successor[1]]

                    #Caluclate the A* Cost associated with getting to the successor state to be pushed onto the fringe
                    a_star_cost = problem.getCostOfActions(action_list) + heuristic(successor[0], problem)
                    fringe.update((successor[0],action_list), a_star_cost)
                    #action_fringe.update(action_list, a_star_cost)
    return actions_path
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
