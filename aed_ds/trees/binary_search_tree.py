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
        if not self.get_root():
            raise NoSuchElementException()

        elif self.get_root().get_key() == k:
            return self.get_root().get_element()

        else:
            result = self.recursive_get_node_root(self.get_root(), k)
            if not result:
                print(result)
                raise NoSuchElementException()

            elif k < result.get_key():
                result = result.get_left_child()

            else:
                result = result.get_right_child()

            return result.get_element()

    def get_node(self, k):
        if not self.get_root():
            raise NoSuchElementException()

        elif self.get_root().get_key() == k:
            return self.get_root().get_element()

        else:
            result = self.recursive_get_node_root(self.get_root(), k)
            if not result:
                print(result)
                raise NoSuchElementException()

            elif k < result.get_key():
                result = result.get_left_child()

            else:
                result = result.get_right_child()

            return result

    def get_node_root(self, k):
        if self.get_root().get_element() == k:
            return None
        return self.recursive_get_node_root(self.get_root(), k)

    def recursive_get_node_root(self, current_node, k, previus_node=None):
        if current_node:
            current_key = current_node.get_key()
            if current_key == k:
                return previus_node

            if k < current_key:
                return self.recursive_get_node_root(current_node.get_left_child(), k, current_node)
            elif k > current_key:
                return self.recursive_get_node_root(current_node.get_right_child(), k, current_node)

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException

    def insert(self, k, v):
        self.root = self.insert_element(self.root, k, v)

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k):
        node_to_remove = self.get_node(k)
        previous_node = self.get_node_root(k)

        if node_to_remove.is_leaf():
            if not previous_node:
                self.root = None
            elif previous_node.get_key() < k:
                previous_node.set_right_child(None)
            else:
                previous_node.set_left_child(None)

        elif not node_to_remove.get_right_child():
            if not previous_node:
                self.root = previous_node.get_left_child()

            elif previous_node.get_key() < k:
                previous_node.set_right_child(None)
            else:
                previous_node.set_left_child(node_to_remove.get_left_child())

        else:
            left_element = self.remove_element(node_to_remove, node_to_remove)

            if previous_node:
                if previous_node.get_key() < k:
                    previous_node.set_right_child(left_element)
                else:
                    previous_node.set_left_child(left_element)

            left_element.set_left_child(node_to_remove.get_left_child())
            left_element.set_right_child(node_to_remove.get_right_child())

    def remove_element(self, current_node, previous_node=None):
        if not current_node.get_left_child():
            previous_node.set_left_child(current_node.get_right_child())
            return current_node
        else:
            self.remove_element(current_node.get_left_child(), current_node)

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
