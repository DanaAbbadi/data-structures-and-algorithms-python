# Depth-first method

Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, a node may be visited twice. To avoid processing a node more than once, use a boolean visited array.

_______________________________________________________________________

## Challenge

Implement a depth-first traversal on a graph.

**Input:** adjacency list as a graph.

**Output:** list of nodes in their pre-order depth-first traversal order

_________________________________________________________________

## Algorithm:

1. Create a recursive function that takes a node
2. Mark the current node as visited and append it to the list
3. Traverse all the adjacent and unmarked nodes and call the recursive function with the next node.

____________________________________________________________________________________

## Whiteboard

![graph](/assets/graphdepth.PNG)