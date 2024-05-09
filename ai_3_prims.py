from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def greedy_prim_mst(self):
        visited = set()
        mst = []

        # Choose any starting vertex
        start_vertex = next(iter(self.graph))

        # Add the starting vertex to the visited set
        visited.add(start_vertex)

        while len(visited) < len(self.graph):
            min_edge = None
            min_weight = float('inf')

            # Find the minimum weight edge from visited vertices to unvisited vertices
            for u in visited:
                for v, weight in self.graph[u]:
                    if v not in visited and weight < min_weight:
                        min_edge = (u, v)
                        min_weight = weight

            # Add the minimum weight edge to the MST
            if min_edge:
                u, v = min_edge
                mst.append((u, v, min_weight))
                visited.add(v)

        return mst

# Example usage:
g = Graph()
g.add_edge('a', 'b', 2)
g.add_edge('a', 'c', 3)
g.add_edge('a', 'd', 3)
g.add_edge('b', 'c', 4)
g.add_edge('b', 'e', 3)
g.add_edge('c', 'e', 1)
g.add_edge('c', 'f', 6)
g.add_edge('c', 'd', 5)
g.add_edge('d', 'f', 7)
g.add_edge('e', 'f', 8)
g.add_edge('f', 'g', 9)

mst = g.greedy_prim_mst()
total_weight = sum(weight for _, _, weight in mst)

print("Edges in the Minimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"{u} - {v} : {weight}")

print("\nTotal weight of the MST:", total_weight)
