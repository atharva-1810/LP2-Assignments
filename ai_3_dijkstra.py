# -*- coding: utf-8 -*-
"""AI_3_Dijkstra.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gs2Qhxz2Y30BfAetYFFkn6ojiUYz0uuk
"""

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]  # (distance, node)

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def main():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        start, end, weight = input("Enter start node, end node, and weight separated by space: ").split()
        weight = int(weight)

        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}

        graph[start][end] = weight
        graph[end][start] = weight

    start_node = input("Enter the start node: ")
    distances = dijkstra(graph, start_node)

    print("Shortest distances from", start_node, ":")
    for node, distance in distances.items():
        print(f"To {node}: {distance}")

if __name__ == "__main__":
    main()