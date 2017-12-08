.. _graph:

Graph
=====

Python graph library:

* http://networkx.github.io/

(Python) graph sites:

* https://www.python.org/doc/essays/graphs/
* https://wiki.python.org/moin/PythonGraphApi
* http://www.linux.it/~della/GraphABC/
* https://www.python-course.eu/graphs_python.php
* `<https://en.wikipedia.org/wiki/Graph_(abstract_data_type)>`_
* https://en.wikipedia.org/wiki/Adjacency_list
* http://www.ics.uci.edu/~eppstein/161/960201.html
* https://pkch.io/2017/03/31/python-graphs-part1/
* https://pkch.io/2017/04/12/python-graphs-part2/

Molecular graph can not be directly defined in python as comparable atoms
connected with chemical bonds, because of python invariant that *equal objects
have same hash value*.

This can be explained on a **1-1** example::

    >>> import networkx as nx
    >>> graph = nx.Graph()
    >>> graph.add_edge(1, 1)

    >>> graph.nodes()
    [1]
    >>> graph.edges()
    [(1, 1)]

What we built instead of **1-1** is a multigraph with a self loop **1]**.

Let us now look at chemical example of ethane: **H3CCH3**.
As you can see, we have 2 carbons (C), and 6 hydrogens (H)::

    >>> import networkx as nx
    >>> ethane = nx.Graph()
    >>> ethane.add_edge("C", "C")
    >>> for __ in range(6):
    ...     ethane.add_edge("H", "C")

    >>> S = sorted
    >>> S(ethane.nodes())
    ['C', 'H']

    >>> S(S((left, right)) for left, right in ethane.edges())
    [['C', 'C'], ['C', 'H']]

We got **H-C]**.
We can separately track atoms, and use list indices as nodes::

    >>> import networkx as nx

    >>> #        0 2 4 6 
    >>> atoms = "HHHHHHCC"
    >>> ethane = nx.Graph()

    >>> #               C  C
    >>> ethane.add_edge(6, 7)
    >>> for i in range(2):
    ...     for H in range(3):
    ... #                         H     C
    ...         ethane.add_edge(H+i*3, i+6)
    ...

    >>> # nodes from atoms mapping
    >>> for i in sorted(ethane.nodes()):
    ...     print(atoms[i], end=" ")
    ...
    H H H H H H C C 

    >>> # edges from atoms mapping
    >>> for i, j in ethane.edges():
    ...     print(atoms[i], "-", atoms[j], sep="", end=" ")
    ...
    C-C C-H C-H C-H C-H C-H C-H 


What we really need is::

    >>> from pybio.tools.graph import Graph
    >>> ethane = Graph()

    >>> # add carbons and keep corresponding nodes
    >>> C1, C2 = C = [ethane.nodes.add("C") for __ in range(2)]

    >>> # add hydrogens and keep corresponding nodes
    >>> H = [ethane.nodes.add("H") for __ in range(6)]

    >>> # bind carbons
    >>> ethane.edges[C1, C2] = True

    >>> # connect 3 hydrogen atoms per carbon atom
    >>> for i in range(2):
    ...     for j in range(3):
    ...         ethane.edges[C[i], H[i*3 + j]] = True
    ...

    >>> # membership testing
    >>> "C" in ethane
    True
    >>> C1 in ethane
    True

    >>> for node in sorted(ethane.nodes, key=lambda node: node()):
    ...     print(node(), end=" ")
    ...
    C C H H H H H H 

    >>> # Node comparison
    >>> C1 is C2, C1 == C2
    (False, False)

    >>> # Values comparison
    >>> C1() is C2(), C1() == C2()
    (True, True)

    >>> S = sorted
    >>> for edge in S(S([left(), right()]) for left, right in ethane.edges):
    ...     print("{}-{}".format(*edge), end=" ")
    ...
    C-C C-H C-H C-H C-H C-H C-H 

