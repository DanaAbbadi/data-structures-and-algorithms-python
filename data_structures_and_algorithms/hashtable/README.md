# Hashtables

A hash table is a data structure that is used to store keys/value pairs. It uses a hash function to compute an index into an array in which an element will be inserted or searched. By using a good hash function, hashing can work well. Under reasonable assumptions, the average time required to search for an element in a hash table is O(1).

_______________________________

## Challenge

The challenge with Hashtables is how to handle collisions, where different keys will be hashed to result in the same location.

One way to solve this is by using **chaining**. Chaining is the idea of formatting linked lists on all collisions. If you want to retrieve that specific information you’d have to traverse the linked list. For example, in the chart bellow John Smith and Sandra Dee are indeed colliding, but using chaining we can retrieve the right data.

![collision](https://miro.medium.com/max/563/0*T0qH-3nO0rELcvhI.png)

____________________________

## Implementation

##### The Hashtable is implemented with the following methods:

* **hash:** takes in an arbitrary key and returns an index in the collection.
* **add:** takes in both the key and value. This method hashes the key, and adds the key and value pair to the table, handling collisions as needed.
* **get:** takes in the key and returns the value from the table.
* **contains:** takes in the key and returns a boolean, indicating if the key exists in the table already.

________________________________

## Testing

The Hashtable implementation passes the following tests:

1. Adding a key/value to your hashtable results in the value being in the data structure
2. Retrieving based on a key returns the value stored
3. Successfully returns null for a key that does not exist in the hashtable
4. Successfully handle a collision within the hashtable
5. Successfully retrieve a value from a bucket within the hashtable that has a collision
6. Successfully hash a key to an in-range value
______________________________________

## Whiteboard


<img src= '/assets/hashtable.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>