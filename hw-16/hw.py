from typing import List, Any, Dict, Set, Generator


class StaticArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [] * self.capacity

    def set(self, index: int, value: int) -> None:
        self.array[index] = value

    def get(self, index: int) -> int:
        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of bounds")
        return self.array[index]


class DynamicArray:
    def __init__(self):
        self.array = []
        self.size = 0

    def append(self, value: int) -> None:
        self.array.append(value)
        self.size += 1

    def insert(self, index: int, value: int) -> None:
        self.array.insert(index, value)
        self.size += 1

    def delete(self, index: int) -> None:
        del self.array[index]
        self.size -= 1

    def get(self, index: int) -> int:
        return self.array[index]


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        pass


    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """

    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
    
    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
    
    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """

class DoubleNode:
    def __init__(self, value: int, next_node = None, prev_node = None):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """

    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
    
    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
    
    def get_head(self) -> DoubleNode:
        """
        Returns the head node of the linked list.
        """
    
    def get_tail(self) -> DoubleNode:
        """
        Returns the tail node of the linked list.
        """

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value: int) -> None:
        self.queue.append(value)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0



class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """

    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """
    
    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """

    def height(self) -> int:
        """
        Returns the height of the tree.
        """

    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the tree.
        """

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the tree.
        """

    def level_order_traversal(self) -> List[int]:
        """
        Perform a level order (breadth-first) traversal of the tree.
        """

    def minimum(self) -> TreeNode:
        """
        Returns the node with the minimum value in the tree.
        """

    def maximum(self) -> TreeNode:
        """
        Returns the node with the maximum value in the tree.
        """
    
    def is_valid_bst(self) -> bool:
        """
        Check if the tree is a valid binary search tree.
        """

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    return lst

def selection_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

def shell_sort(lst: List[int]) -> List[int]:
    pass

def merge_sort(lst: List[int]) -> List[int]:
    pass

def quick_sort(lst: List[int]) -> List[int]:
    pass
