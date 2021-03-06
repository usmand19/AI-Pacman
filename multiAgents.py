# multiAgents.py
# --------------
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


import random

import util
from game import Agent, Directions  # noqa
from util import manhattanDistance  # noqa


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()

        
        distances = []
        food_List = newFood.asList()
        min_distance = -1 * float('inf')
        # Choose smallest for initialized value:
        for food in food_List:
          distances += [util.manhattanDistance(newPos, food)]
          # replace value with a lower value if possible (or initialize if equal to negatve infinity)
          for d in distances:
            if min_distance == -1 * float('inf') or min_distance>= d:
              min_distance = min(distances)


        """Calculating the distances from pacman to the ghosts. Also, checking for the proximity of the ghosts (at distance of 1) around pacman."""
        # Calculate the distance from pacman to each ghost
        # Use a small value to avoid division by zero error
        ghost_distance_total = 0.001
        ghost_penalty = 0
        for ghost in successorGameState.getGhostPositions():
            ghost_distance_total += util.manhattanDistance(newPos, ghost)
          #Put penalty to avoid all ghosts at all costs:
            if util.manhattanDistance(newPos, ghost)  == 1:
              ghost_penalty += 1e6

        added_score = (1/float(min_distance)) + -1 * ((1 / float(ghost_distance_total)) + (ghost_penalty))
        return successorGameState.getScore() + added_score


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn="scoreEvaluationFunction", depth="2"):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """


        def minimax(agent_Index, game_State, depth):
          if game_State.isLose() or game_State.isWin() or depth == self.depth:
            return self.evaluationFunction(game_State)
          if agent_Index == 0:
            # update pacman to be a ghost state
            next_Agent = agent_Index + 1
            # Call minimax again for ghosts, each branch is a game state from the successors of the action taken by pacman
            v = max(minimax(next_Agent, game_State.generateSuccessor(agent_Index, new_GameState),depth) for new_GameState in game_State.getLegalActions(agent_Index))
            return v
          else:
            #update tot he next agent
            next_Agent = agent_Index + 1
            if game_State.getNumAgents() == next_Agent:
              next_Agent = 0
          # Also update (increment) the depth of the tree everytime we see the max agent (pacman's turn to move)
            if next_Agent == 0:
              depth += 1
            # Call minimax again for the next ghost (up to 'depth'), with each branch is generated from a game state from the successors of the action taken by the current ghost
            return min(minimax(next_Agent, game_State.generateSuccessor(agent_Index, new_GameState),depth) for new_GameState in game_State.getLegalActions(agent_Index))
            
        # Initialize root node
        #use Negative infinity since root of tree is Max node
        v = float("-inf")
        for agentState in gameState.getLegalActions(0):
            utility = minimax(1, gameState.generateSuccessor(0, agentState), 0)
            if utility > v or v == float("-inf"):
              #We take maximum of possible nodes as our action, and update the value of the root (v)
                v = utility
                # Set current decsion as the maximum we have observed so far
                decision = agentState

        return decision


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction
