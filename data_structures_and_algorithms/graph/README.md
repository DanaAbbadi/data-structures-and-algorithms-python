# Graph 

______________________________________________

## Overview

A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges. The various terms and functionalities associated with a graph is described in great detail in our tutorial here. In this chapter we are going to see how to create a graph and add various data elements to it using a python program.

**Here is some common terminology used when working with Graphs:**

* **Vertex** - A vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.
* **Edge** - An edge is a connection between two nodes.
* **Neighbor** - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.
* **Degree** - The degree of a vertex is the number of edges connected to that vertex.

____________________________________________________

## Challenge

Implement a graph, the graph should be represented as an adjacency list, with the ability to add new vertices, add thier edgees, and retrieve the all nodes and neighbors.

_______________________________________________________________________

## API

The graph class is implemented with the following methods:

### add_node():

   * Adds a new node to the graph.
   * Takes in the value of that node.
   * Returns the added node.

### add_edge():

   * Adds a new edge between two nodes in the graph.
   * Include the ability to have a “weight”.
   * Takes in the two nodes to be connected by the edge.
       * Both nodes should already be in the Graph.


### get_nodes():

   * Returns all of the vertexes in the graph as a collection.

### get_neighbors():

   * Returns a collection of edges connected to the given node.
   * Takes in a given node.
   * Include the weight of the connection in the returned collection.

### size():

   * Returns the total number of nodes in the graph.

__________________________________________________________________

## Approach & Efficiency

The Big O for all methods is : 

| Time Complexity | Space Complexity |
|------|--------|
| Big O(1) | Big O(1)|
________________________________________________________________

## Verification

The graph class passes the following tests successfully:

1. Node can be successfully added to the graph
1. An edge can be successfully added to the graph
1. A collection of all nodes can be properly retrieved from the graph
1. All appropriate neighbors can be retrieved from the graph
1. Neighbors are returned with the weight between nodes included
1. The proper size is returned, representing the number of nodes in the graph
1. A graph with only one node and edge can be properly returned
1. An empty graph properly returns null

____________________________________________________________________________

## Whiteboard

![graph](/assets/graph.PNG)

____________________________________________________________

# Breadth-first method

Breadth First Search (BFS) algorithm traverses a graph in a breadthward motion and uses a queue to remember to get the next vertex to start a search, when a dead end occurs in any iteration.

![breadth](https://www.tutorialspoint.com/data_structures_algorithms/images/breadth_first_traversal.jpg)

As in the example given above, BFS algorithm traverses from A to B to E to F first then to C and G lastly to D. It employs the following rules.

  - **Rule 1** − Visit the adjacent unvisited vertex. Mark it as visited. Display it. Insert it in a queue.
  
  - **Rule 2** − If no adjacent vertex is found, remove the first vertex from the queue.
  
  - **Rule 3** − Repeat Rule 1 and Rule 2 until the queue is empty.


_______________________________________________________________________

## Challenge

Implement a breadth-first traversal on a graph.

**Input:** node in the graph, to start traversing from.

**Output:** list of nodes staring from the given node, in the breadth-first approach.

____________________________________________________________________________________

## Whiteboard

![graph](/assets/graphbreadth.PNG)
