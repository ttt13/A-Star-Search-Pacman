# Pacman A* Search
In this program, pacman will find paths through the maze world to either reach a particular location or find food in the most efficent way. The user may select three searches: Depth First Search, Breadth First Search, and A* Search.

## Pathfinding using Depth First Search
The graph search version of Depth First Search is implemented. This version will avoid expanding states that have already been visited.
Depth First Search should be able to find paths for the following:
```python pacman.py -l tinyMaze -p SearchAgent```

```python pacman.py -l mediumMaze -p SearchAgent```

```python pacman.py -l bigMaze -z .5 -p SearchAgent```

## Pathfinding using Breadth First Search
The graph search version of Breadth First Search is implementing, so states that have already been visited will not be expanded. BFS can be tested by running the following commands:

```python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs```

```python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5```

## Pathfinding using A* Search
A* takes a heuristic function as an argument. This implementation uses the [Manhattan Distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html) as the heuristic. The algorithm can be tested using the following:

```python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic```

## Finding food using A* Search
```python pacman.py -l mediumCorners -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5```
