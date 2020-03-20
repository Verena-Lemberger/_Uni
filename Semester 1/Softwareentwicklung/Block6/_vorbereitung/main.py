import astar_search as search
import graph_node as gn
import graph_heuristik


rootnode = gn.GraphNode(None, "Frankfurt")
node = search.astar_search(rootnode, graph_heuristik.h1)

path = []

while True:
    if node:
        path.append(node)

    node = node.parent

    if node == None:
        break


path.reverse()
for node in path:
    print(node.unique, node.path_cost)

