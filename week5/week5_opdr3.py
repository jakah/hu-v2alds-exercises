from BFS import Vertex
from BFS import edges
from BFS import vertices
from BFS import path_BFS
from BFS import BFS


def get_bridges(G):
    """Get all bridges in a graph.

    Args:
        G (Graph): Graph to check.

    Returns:
        List: List with tuples of bridges.
    """
    a = []
    for v, u in edges(G):
        G[v].remove(u)
        BFS(G, u)
        if path_BFS(G, v, u) == [u]:
            a.append((v, u))
        G[v].append(u)
    return a


v = [Vertex(i) for i in range(8)]

with_bridges = {v[0]: [v[1], v[3]],
                v[1]: [v[0], v[2]],
                v[2]: [v[1], v[3], v[4]],
                v[3]: [v[0], v[2]],
                v[4]: [v[2], v[5], v[6]],
                v[5]: [v[4], v[6]],
                v[6]: [v[4], v[5], v[7]],
                v[7]: [v[6]]}

# print("Old")
# print(edges(with_bridges))
# print(with_bridges)
print(get_bridges(with_bridges))
# print("New")
# print(edges(with_bridges))
# print(with_bridges)
