import random
import time
import matplotlib.pyplot as plt

from dijkstra import dijkstra


def generate_graph(num_nodes, edges_per_node=3):

    graph = {}

    # Create nodes
    for i in range(num_nodes):
        graph[i] = {}

    # Create random edges
    for i in range(num_nodes):

        for _ in range(edges_per_node):

            j = random.randint(0, num_nodes - 1)

            if i != j:
                weight = random.randint(1, 100)

                graph[i][j] = weight
                graph[j][i] = weight

    return graph


def measure_time(graph):

    start_node = 0
    destination = len(graph) - 1

    start_time = time.perf_counter()

    dijkstra(
        graph,
        start_node,
        destination
    )

    end_time = time.perf_counter()

    return end_time - start_time


# Different graph sizes
sizes = [
    10,
    50,
    100,
    500,
    1000
]

times = []


print("Dijkstra Performance")
print("-" * 40)


for size in sizes:

    graph = generate_graph(size)

    duration = measure_time(graph)

    times.append(duration)

    print(
        f"Nodes: {size:5d} | "
        f"Time: {duration:.6f} seconds"
    )


# Plot the results

plt.figure(figsize=(10, 6))

plt.plot(
    sizes,
    times,
    marker="o"
)

plt.title("Dijkstra's Algorithm Performance")

plt.xlabel("Number of Nodes (V)")

plt.ylabel("Execution Time (seconds)")

plt.grid(True)

plt.tight_layout()

plt.show()