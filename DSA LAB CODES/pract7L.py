# You have a business with several offices; you want to lease phone lines to connect them up with each other; and the phone company charges different amounts of money to connect different pairs of cities. You want a set of lines that connects all your offices with a minimum total cost. Solve the problem by suggesting appropriate data structures.

import heapq

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination, cost):
        self.adj_list[source].append((destination, cost))
        self.adj_list[destination].append((source, cost))


def find_minimum_spanning_tree(graph):
    visited = set()
    mst_edges = []
    priority_queue = []
    
    # Start with any vertex (e.g., vertex 0)
    start_vertex = 0
    visited.add(start_vertex)
    
    # Add all the edges of the start_vertex to the priority queue
    for neighbor, cost in graph.adj_list[start_vertex]:
        priority_queue.append((cost, start_vertex, neighbor))
    heapq.heapify(priority_queue)
    
    while priority_queue:
        cost, source, destination = heapq.heappop(priority_queue)
        
        # Check if adding the edge creates a cycle
        if destination in visited:
            continue
        
        # Add the edge to the MST
        mst_edges.append((source, destination, cost))
        visited.add(destination)
        
        # Add all the edges of the destination to the priority queue
        for neighbor, cost in graph.adj_list[destination]:
            heapq.heappush(priority_queue, (cost, destination, neighbor))
    
    return mst_edges


# Example usage:
g = Graph(6)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 1)
g.add_edge(2, 4, 3)
g.add_edge(3, 4, 5)
g.add_edge(3, 5, 2)

mst_edges = find_minimum_spanning_tree(g)
total_cost = sum(cost for _, _, cost in mst_edges)

print("Minimum Spanning Tree Edges:")
for source, destination, cost in mst_edges:
    print(f"{source} - {destination}, Cost: {cost}")

print(f"Total Cost: {total_cost}")
