from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..exceptions import DuplicatedKeyException, NoSuchElementException, \
    EmptyDictionaryException
from .nodes.binary_nodes import BinarySearchTreeNode
from .binary_search_tree_iterator import Iterator


class BinarySearchTree(OrderedDictionary, Tree):
    def __init__(self):
        self.root = BinarySearchTreeNode()
        self.count = 0
        self.levels = None

    # Returns the number of elements in the dictionary.
    def size(self):
        return self.count

    # Returns true if the dictionary is full.
    def is_full(self):
        return False

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k):
        pass
    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException

    def insert(self, k, v):
        self.root = self.insert_element(self.root, k, v)

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k): pass

    # Returns a List with all the keys in the dictionary.
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List with all the key value pairs in the dictionary.
    def items(self): pass

    # Returns an iterator of the elements in the dictionary
    def iterator(self):
        return Iterator(self.root)

    # Returns the element with the smallest key
    # Throws EmptyTreeException

    def get_min_element(self):
        if self.is_empty():
            raise EmptyDictionaryException()
        return self.get_min_node(self.root).get_element()

    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_element(self):
        if self.is_empty():
            raise EmptyDictionaryException()
        return self.get_max_node(self.root).get_element()

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self):
        return self.root.get_element()

    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self):
        return self.levels

    # Returns True if the tree is empty
    def is_empty(self):
        return self.count == 0

    def get_min_node(self, root):
        if root.get_left_child() is None:
            return root
        return self.get_min_node(root.get_left_child())

    def get_max_node(self, root):
        if root.get_right_child() is None:
            return root
        return self.get_max_node(root.get_right_child())

    def insert_element(self, root, k, v):
        if root is None:
            root = BinaryTreeNode(k, v)
            self.count += 1
        else:
            if root.get_key() == k:
                raise DuplicatedKeyException()
            elif root.get_key() > k:
                node = self.insert_element(root.get_left_child(), k, v)
                root.set_left_child(node)
            else:
                node = self.insert_element(root.get_right_child(), k, v)
                root.set_right_child(node)
        return root
