from BFS import Vertex
from BFS import BFS
from math import inf as INFINITY
from BFS import edges
from BFS import vertices
from BFS import path_BFS
from BFS import myqueue


def no_cycles(G):
    """Check if a graph contains cycles

    Args:
        G (Graph): Graph that will be checked.

    Returns:
        boolean: True when a graph has no cycles. False when a graph has cycles.
    """
    V = vertices(G)
    s = vertices(G)[0]
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)

    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)
            elif u.predecessor != v:
                return False  # Graph bevat een cycle
    return True  # Graph bevat geen cycle


v = [Vertex(i) for i in range(8)]

without_cycles = {v[0]: [v[4], v[5]],
                  v[1]: [v[4], v[6]],
                  v[2]: [v[5]],
                  v[3]: [v[7]],
                  v[4]: [v[0], v[1]],
                  v[5]: [v[0], v[2]],
                  v[6]: [v[1]],
                  v[7]: [v[3]]}

with_cycles = {v[0]: [v[1], v[4]],
               v[1]: [v[0], v[5]],
               v[2]: [v[3], v[5], v[6]],
               v[3]: [v[2], v[6], v[7]],
               v[4]: [v[0]],
               v[5]: [v[1], v[2], v[6]],
               v[6]: [v[2], v[3], v[5], v[7]],
               v[7]: [v[3], v[6]]}
print("Without cycle")
print(no_cycles(without_cycles))
print("With cycle")
print(no_cycles(with_cycles))
