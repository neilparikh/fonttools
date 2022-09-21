import itertools

class Node():
    def __init__(self, lines, name):
        self.lines = lines
        self.name = name

    def render(self):
        result = ""
        result += "  %s [\n" % (self.name)
        result += "    label=<%s>\n" % ("<BR/>".join(self.lines))
        result += "    shape=box\n"
        result += "  ]\n"
        return result

class Edge():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def render(self):
        result = ""
        result += "  %s -> %s" % (self.a, self.b)
        return result

class Graph():
    newID = itertools.count(1)

    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, lines):
        name = str(Graph.newID.next())
        node = Node(lines, name)
        self.nodes.append(node)
        return name

    def addEdge(self, a, b):
        self.edges.append(Edge(a, b))

    def render(self):
        result = ""
        result += "digraph G {\n"

        result += "  # Nodes\n"
        for node in self.nodes:
            result += node.render() + "\n"
        result += "\n  # Edges\n"

        for edge in self.edges:
            result += edge.render() + "\n"

        result += "}"
        return result
