graph = {
    "Frankfurt": {
        "Würzburg": 111,
        "Mannheim": 85
    },
    "Mannheim": {
        "Nürnberg": 230,
        "Frankfurt": 85,
        "Karlsruhe": 67
    },
    "Landeck": {
        "Innsbruck": 73
    },
    "Innsbruck": {
        "Landeck": 73,
        "Rosenheim": 93
    },
    "Rosenheim": {
        "Innsbruck": 93,
        "Salzburg": 81,
        "München": 59
    },
    "Salzburg": {
        "Rosenheim": 81,
        "Linz": 126,
    },
    "Linz": {
        "Salzburg": 126,
        "Passau": 102
    },
    "Passau": {
        "Linz": 102,
        "Nürnberg": 220,
        "München": 189
    },
    "Nürnberg": {
        "Passau": 220,
        "Bayreuth": 75,
        "Würzburg": 104,
        "Ulm": 171,
        "München": 170,
        "Mannheim": 230
    },
    "Ulm": {
        "Nürnberg": 171,
        "Stuttgart": 107,
        "Memmingen": 55,
        "München": 123
    },
    "München": {
        "Ulm": 123,
        "Memmingen": 115,
        "Nürnberg": 170,
        "Passau": 102,
        "Rosenheim": 59
    },
    "Memmingen": {
        "München": 115,
        "Zürich": 184,
        "Ulm": 55
    },
    "Zürich": {
        "Memmingen": 184,
        "Basel": 85,
        "Bern": 120
    },
    "Bern": {
        "Basel": 91,
        "Zürich": 120
    },
    "Basel": {
        "Zürich": 85,
        "Bern": 91
    },
    "Karlsruhe": {
        "Basel": 191,
        "Mannheim": 67,
        "Stuttgart": 64
    },
    "Stuttgart": {
        "Karlsruhe": 64,
        "Würzburg": 140,
        "Ulm": 107
    },
    "Bayreuth": {
        "Nürnberg": 75
    },
    "Würzburg": {
        "Frankfurt": 111,
        "Stuttgart": 140,
        "Ulm": 183,
        "Nürnberg": 104
    }
}

class GraphNode:
    def __init__(self, parent, state, path_cost = 0):
        self.parent = parent
        self.state = state
        self.path_cost = path_cost

    @property
    def unique(self):
        return self.state
    
    def is_goal_node(self):
        return self.state == "Ulm"

    def get_child_nodes(self):
        child_nodes = []
        node = graph.get(self.state)

        for child in node:
            child_nodes.append(GraphNode(self, child, self.path_cost + node.get(child)))

        return child_nodes