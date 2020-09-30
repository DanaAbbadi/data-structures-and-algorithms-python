# Left Join

Author: Dana Al-abbade

_______________________________________

## Problem Domain

Write a function that LEFT JOINs two hashmaps into a single data structure.

LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.

___________________________________

## Algorithm

1. Create an empty array to store the output
2. Loop through the keys in the first dictionary.
3. Each iteration, check if the key exists in the second dictionary, if it does then append it to the list.
4. Else append the key, its value and Null.

________________________________________

## Approach & Efficiency

**Time** Big O(n).

**Space** Big O(n).

____________________________________________________

## Whiteboard

<img src= '/assets/dictionary.PNG' style = 'display: block; margin-left: auto;   margin-right: auto; width: 50%; '>