# Min Heap Implementation in Python

This project provides a simple **Min Heap** implementation using a Python class and an array-based complete binary tree representation.

##  Features

- **Array-based storage** for efficient memory usage.
- **Complete Binary Tree** structure.
- **Heapify Down** method for restoring the heap property.
- **Build Heap** method to convert an unsorted array into a valid min heap.

##  How It Works

A **Min Heap** is a binary tree where:
- Every parent node is **less than or equal to** its children.
- The tree is **complete** (all levels are fully filled except possibly the last, which fills left to right).

We represent the heap as an array:
- **Root** is at index `0`.
- **Left child** of node at index `i`: `2*i + 1`
- **Right child** of node at index `i`: `2*i + 2`
- **Parent** of node at index `i`: `(i - 1) // 2`

##  Class Methods

### `__init__(self)`
Initializes an empty heap.

### `left_child(self, i)`
Returns the index of the left child of node at index `i`.

### `right_child(self, i)`
Returns the index of the right child of node at index `i`.

### `parent(self, i)`
Returns the index of the parent node of index `i`.

### `build_heap(self)`
- Builds a valid min heap from the current `self.data` array.
- Starts from the **last parent** node and calls `heapify_down` on each node up to the root.

### `heapify_down(self, i)`
- Restores the heap property by moving the element at index `i` **down** to its correct position.
- Swaps the element with its smallest child until the min heap property is satisfied.


print(heap.data)  # Output: Min heap array representation
