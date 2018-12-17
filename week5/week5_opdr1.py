from BFS import Vertex
from BFS import BFS
from math import inf as INFINITY


def is_connected(G):
    """Check if undirected graph is connected. 

    Args:
        G (graph): Graph that will be checked.

    Returns:
        Boolean: False when not connected else True.
    """
    BFS(G,v[0])
    for x in G:
        if x.distance == INFINITY:
            return False
    return True

v = [Vertex(i) for i in range(8)]

G = {v[0]: [v[1], v[4]],
     v[1]: [v[0], v[5]],
     v[2]: [v[3], v[5], v[6]],
     v[3]: [v[2], v[6], v[7]],
     v[4]: [v[0]],
     v[5]: [v[1], v[2], v[6]],
     v[6]: [v[2], v[3], v[5], v[7]],
     v[7]: [v[3], v[6]]}

H = {v[0]: [v[1], v[4]],
     v[2]: [v[3], v[5], v[6]],
     v[3]: [v[2], v[6], v[7]],
     v[4]: [v[0]],
     v[5]: [v[1], v[2], v[6]],
     v[6]: [v[2], v[3], v[5], v[7]],
     v[7]: [v[3], v[6]]}

print(is_connected(G))
print(is_connected(H))
