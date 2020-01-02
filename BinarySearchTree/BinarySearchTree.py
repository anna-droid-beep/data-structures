from SelfImplementedQueue.Queue import Queue
from BinarySearchTree.TreeTraversalOrder import TreeTraversalOrder

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None, node_count=0):
        self.root = root
        self.node_count = node_count

    def is_empty(self):
        return self.get_size() == 0

    def get_size(self):
        return self.node_count

    def add(self, data):
        if self.contains(data):
            return False
        else:
            self.root = self._add(self.root, data)
            self.node_count += 1
            return True

    def contains(self, data):
        node, _ = self._find_iterative(self.root, self.root, data)
        return node is not None

    def height(self):
        return self._height(self.root)

    def traverse(self, strategy):
        if self.is_empty():
            return '{ }'
        elems = list()
        if strategy == TreeTraversalOrder.PRE_ORDER:
            self._pre_order(self.root, elems)
        elif strategy == TreeTraversalOrder.IN_ORDER:
            self._in_order(self.root, elems)
        elif strategy == TreeTraversalOrder.POST_ORDER:
            self._post_order(self.root, elems)
        elif strategy == TreeTraversalOrder.LEVEL_ORDER:
            self._bfs(elems)
        else:
            raise ValueError("Tree traversal strategy does not exist. "
                             "Current implementations are {}. Was {}".format(TreeTraversalOrder.values(), strategy))
        printed = '{{ {} }}'.format(' '.join(elems))
        return printed

    def _bfs(self, elems):
        if self.is_empty():
            return "{ }"
        q = Queue()
        q.enqueue(self.root)
        while q.is_empty() is False:
            node = q.dequeue()
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            elems.append(str(node.data))
        return elems

    def _in_order(self, node, elems):
        if node is None:
            return elems
        self._in_order(node.left, elems)
        elems.append(str(node.data))
        self._in_order(node.right, elems)

    def _pre_order(self, node, elems):
        if node is None:
            return elems
        elems.append(str(node.data))
        self._pre_order(node.left, elems)
        self._pre_order(node.right, elems)

    def _post_order(self, node, elems):
        if node is None:
            return elems
        self._post_order(node.left, elems)
        self._post_order(node.right, elems)
        elems.append(str(node.data))


    def remove(self, data):
        node, parent = self._find_iterative(self.root, self.root, data)
        if node is None:
            return False
        else:
            self._remove_iterative(node, parent)
            self.node_count -= 1
            return True

    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1

    def _add(self, node, data):
        if node is None:
           node = Node(data, None, None)
        else:
            if data < node.data:
                node.left = self._add(node.left, data)
            else:
                node.right = self._add(node.right, data)

        return node

    def _find_iterative(self, node, parent, data):
        if node is None:
            return None, None

        if data == node.data:
            return node, parent
        else:
            parent = node
            if data < node.data:
                node = node.left
            else:
                node = node.right

        return self._find_iterative(node, parent, data)

    def _remove_iterative(self, node, parent=None):
        if node.right and node.left:
            left_most, left_parent = self._find_min_iterative(node.right)
            updated_data = left_most.data
            self._remove_iterative(left_most, left_parent)
            node.data = updated_data
        elif node.right and node.left is None:
            node.data = node.right.data
            node.left = node.right.left
            node.right = node.right.right
        elif node.left and node.right is None:
            node.data = node.left.data
            node.left = node.left.left
            node.right = node.left.right
        else:
            if parent.right is node:
                parent.right = None
            else:
                parent.left = None

    def _find_min_iterative(self, node):
        parent = node
        while node.left:
            parent = node
            node = node.left
        return node, parent

    def _find_max_iterative(self, node):
        parent = node
        while node.right:
            parent = node
            node = node.right
        return node, parent

    def __str__(self):
        return self.traverse(TreeTraversalOrder.LEVEL_ORDER)
