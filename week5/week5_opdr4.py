from BFS import Vertex
from BFS import BFS
from BFS import path_BFS
from BFS import edges
from math import inf as INFINITY

def all_nodes_reachable(G,startnode):
    """Check if all nodes are reachable from the startnode.
    
    Args:
        G (Graph): Graph were all nodes are in.
        startnode (Node): The node all checks are made against
    
    Returns:
        boolean: True when all nodes can be reached, else false
    """
    BFS(G,startnode)
    for search_node in G:
        if search_node.distance == INFINITY:
            return False
    return True
def invert_graph(G):
    """Invert all links in a directed graph.
    
    Args:
        G (Graph): Original directed graph.
    
    Returns:
        Graph: New graph with inverted links.
    """
    H = {}
    for u,v in edges(G):
        if v in H:
            H[v].append(u)
        else:
            H[v] = []
            H[v].append(u)
    return H

def is_strongly_connected(G):
    """Check if a directed graph is strongly connected.
    
    Args:
        G (Graph): Graph that will be checked.
    
    Returns:
        boolean: False when not strongly connected, else True.
    """
    print(G)
    for node in G:
       if not all_nodes_reachable(G,node):
        return False

    for new_node in invert_graph(G):
        if not all_nodes_reachable(G,node):
            return False
    return True

v = [Vertex(i) for i in range(8)]

strongly_connected = {v[0]: [v[1]],
                      v[1]: [v[2]],
                      v[2]: [v[0]]}
not_strongly_connected = {v[0]: [v[1]],
                          v[2]: [v[0], v[1]]}

print(is_strongly_connected(strongly_connected))
print(is_strongly_connected(not_strongly_connected))
