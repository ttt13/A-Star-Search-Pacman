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

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 20
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>
I found this assignment much harder than assignment 0. It was hard because there
where lots of python concepts I did not know.
"""
#####################################################
#####################################################

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
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    visited_nodes = []
    get_start = problem.getStartState()
    directions = []
    # Initialize start state
    fringe.push( (get_start, []) )

    while not fringe.isEmpty():
        coordinates, directions = fringe.pop()
        # Return list of directions when goal met
        if problem.isGoalState(coordinates):
            return directions
        # Track visited states
        if not coordinates in visited_nodes:
            visited_nodes.append(coordinates)
        # Push successors to stack
        for successor, direction, placeholder in problem.getSuccessors(coordinates):
            if not successor in visited_nodes:
                fringe.push( (successor, directions + [direction]) )
            
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Init required tools
    fringe = util.Queue()
    directions = []
    visited_states = []

    #Add start
    get_start = problem.getStartState()
    fringe.push( (get_start, []) )
    visited_states.append(get_start)

    while not fringe.isEmpty():
        
        get_state_xy, directions = fringe.pop()

        if problem.isGoalState(get_state_xy):
            return directions

        else:
            for successor, direction, cost in problem.getSuccessors(get_state_xy):
                # Track visited states
                if not successor in visited_states:
                    visited_states.append(successor)
                    fringe.push((successor, directions + [direction]))
                    #print(directions)
                
    return []
    util.raiseNotDefined()
    


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"

    fringe = util.PriorityQueue()
    start_node = problem.getStartState()
    start_heuristic = heuristic(start_node, problem)
    visited_nodes = []
    fringe.push( (start_node, [], 0), start_heuristic)
    directions = []
    while not fringe.isEmpty():
        get_xy, directions, get_cost = fringe.pop()

        if problem.isGoalState(get_xy):
            return directions
        
        if not get_xy in visited_nodes:
            # Track visited_nodes
            visited_nodes.append(get_xy)
            
            for coordinates, direction, successor_cost in problem.getSuccessors(get_xy):
                if not coordinates in visited_nodes:
                    # Pass by reference
                    actions_list = list(directions)
                    actions_list += [direction]
                    # Get cost so far
                    cost_actions = problem.getCostOfActions(actions_list)
                    get_heuristic = heuristic(coordinates, problem)
                    fringe.push( (coordinates, actions_list, 1), cost_actions + get_heuristic)
    return []
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
