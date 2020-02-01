def astar_search(node, heuristic):
    visited = set()
    queue = []

    while True:
        if(node.is_goal_node()):
            return node

        visited.add(node.unique)
        child_nodes = node.get_child_nodes()

        for child in child_nodes:
            if child.unique not in visited:
                value = child.path_cost + heuristic(child.state)
                queue.append((value, child))

        if len(queue) > 0:
            queue.sort(key = lambda tuple: tuple[0]) # sort by first value in que
            node = queue.pop(0)[1]

        else:
            return None