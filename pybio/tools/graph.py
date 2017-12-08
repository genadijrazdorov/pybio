from collections import abc


class Node(object):
    def __init__(self, value):
        self._value = value

    def __call__(self):
        return self._value

    def __repr__(self):
        return "<Node of {!r}>".format(self())

    def __str__(self):
        return "Node of {}".format(self())


# Graph is modeled similarly to: http://www.linux.it/~della/GraphABC/
# Main difference is in wrapping node values into Node instances.

class Graph(object):
    """undirected graph
    """
    Node = Node

    class NodesView(abc.MutableSet):
        def __init__(self, graph):
            self.graph = graph

        def __contains__(self, node_or_value):
            node = value = node_or_value
            values = lambda: list(self.itervalues())

            return node in self.graph._adj or value in values()

        def __iter__(self):
            return iter(self.graph._adj)

        def __len__(self):
            return len(self.graph._adj)

        def add(self, node):
            if not isinstance(node, Node):
                node = self.graph.Node(node)
                self.graph._adj[node] = {}

            elif node not in self.graph._adj:
                self.graph._adj[node] = {}

            return node

        def discard(self, node):
            adj = self.graph._adj

            try:
                for other in adj[node]:
                    del adj[other][node]

                del adj[node]

            except KeyError:
                pass

        def itervalues(self):
            for node in self:
                yield node() 

        def __repr__(self):
            return repr(set(self))


    class EdgesView(abc.Mapping):
        def __init__(self, graph):
            self.graph = graph

        def __getitem__(self, edge):
            left, right = edge
            return self.graph._adj[left][right]

        def __setitem__(self, edge, value):
            left, right = edge
            left = self.graph.nodes.add(left)
            right = self.graph.nodes.add(right)

            self.graph._adj[left][right] = value
            self.graph._adj[right][left] = value

        def __delitem__(self, edge):
            left, right = edge
            del self.graph._adj[left][right]
            del self.graph._adj[right][left]

        def __iter__(self):
            adj = self.graph._adj
            seen = set()
            for left in adj:
                for right in adj[left]:
                    edge = frozenset({left, right})
                    if edge not in seen:
                        yield edge
                        seen.add(edge)

        def __len__(self):
            l = 0
            for edge in self:
                l += 1
            return l

        def __repr__(self):
            return repr(dict(self))


    def __init__(self):
        # {node: {adjacent_node: incident_edge, ...}, ...}
        self._adj = {}
        self.nodes = self.NodesView(self)
        self.edges = self.EdgesView(self)

    def __contains__(self, node_or_edge):
        node = edge = node_or_edge
        values = lambda: list(self.nodes.itervalues())

        try:
            result = node in self.nodes

        # node is unhashable
        except TypeError:
            result = False

        try:
            result = result or node in values() or edge in self.edges

        # edge is not length 2 iterable
        except (TypeError, ValueError):
            result = False

        return result


    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes)

    # recursive version
    def walk(self, root=None):
        visited = set()
        if root is None:
            # first random node
            root = next(iter(self))

        def _walk(node):
            try:
                yield from node().walk()

            except AttributeError:
                yield node()

            visited.add(node)

            for other in self[node]:
                if other not in visited:
                    yield from _walk(other)

        return _walk(root)

    # non recursive version
    def walk(self, root=None):
        visited = set()
        if root is None:
            # first random node
            root = next(iter(self))

        pending = [root]

        while pending:
            node = pending.pop()
            if node not in visited:
                # add connected
                pending.extend(self[node].keys())
                try:
                    yield from node().walk()

                except AttributeError:
                    yield node()

                visited.add(node)


    def __getitem__(self, node):
        return self._adj[node]

    def edge(self, x, y):
        return self.edges[x, y]

    def __repr__(self):
        return repr(self._adj)
