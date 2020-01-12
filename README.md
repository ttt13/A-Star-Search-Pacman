# Pacman A* Search
In this program, pacman will find paths through the maze world to either reach a particular location or find food in the most efficent way. The user may select three searches: Depth First Search, Breadth First Search, and A* Search.

## Pathfinding using Depth First Search
The graph search version of Depth First Search is implemented. This version will avoid expanding states that have already been visited.
Depth First Search should be able to find paths for the following:
```python pacman.py -l tinyMaze -p SearchAgent```
```python pacman.py -l mediumMaze -p SearchAgent```
```python pacman.py -l bigMaze -z .5 -p SearchAgent```

