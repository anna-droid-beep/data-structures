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

    def add(self, data):
        if self.contains(data):
            return False
        else:
            self.root = self._add(self.root, data)
            self.node_count += 1
            return True

    def _add(self, node, data):
        if node is None:
           node = Node(data, None, None)
        else:
            if data < node.data:
                node.left = self._add(node.left, data)
            else:
                node.right = self._add(node.right, data)

        return node

    def contains(self, data):
        return self._contains(self.root, data)

    def _contains(self, node, data):
        if node is None:
            return False
        if data < node.data:
            return self._contains(node.left, data)
        elif data > node.data:
            return self._contains(node.right, data)
        else:
            return True

    def get_size(self):
        return self.node_count

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1

    def is_empty(self):
        return self.get_size() == 0

    def remove(self, data):
        if self.contains(data):
            self.root = self._remove_recurse(self.root, data)
            self.node_count -= 1
            return True
        else:
            return False

    def _remove_recurse(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self._remove_recurse(node.left, data)
        elif data > node.data:
            node.right = self._remove_recurse(node.right, data)
        else:
            # case where node has only one right subtree or no subtree at all: return the right subtree
            if node.left is None:
                right_child = node.right
                node.data = None
                node.right = None
                return right_child
            # case where node has only one left subtree or no subtree at all: return the left subtree
            elif node.right is None:
                left_child = node.left
                node.data = None
                node.left = None
                return left_child
            # case where node has two subtrees: find the smallest on the right, swap it with the node and remove this
            # smallest node
            else:
                left_most = self._find_min_recursive(node.right)
                node.data = left_most.data
                node.right = self._remove_recurse(node.right, left_most.data)

        return node

    def _find_min_recursive(self, node):
        while node.left:
            node = node.left
        return node

    def _find_max_recursiove(self, node):
        while node.right:
            node = node.right
        return node

    def _remove_iterative(self, node, parent=None):
        """
            Iterative method to remove a node. The benefit of this approach is that we have to find the node
            only once, compared to the recursive method where you have to check the data existence in the public call,
            then refind this node once more in the recursive method. Iterative method is also a good way to prevent from
            Stack Overflow. The limitation of this method comes in the assignment of the 'parent' variable that will
            turned out useless if the node to be removed has a single subtree.
        :param node:
        :param parent:
        :return:
        """
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

    def __str__(self):
        return self.traverse(TreeTraversalOrder.LEVEL_ORDER)
