# PathFinder - Shortest Path Finder
# Dijkstra's Algorithm


# ---------------------------------------------------------
# GRAPH
# ---------------------------------------------------------

# Locations are represented as nodes.
# Roads are represented as edges.
# Numbers represent the distance between locations.

graph = {
    "A": {
        "B": 4,
        "C": 3
    },

    "B": {
        "A": 4,
        "C": 1,
        "D": 2
    },

    "C": {
        "A": 3,
        "B": 1,
        "D": 5,
        "E": 5
    },

    "D": {
        "B": 2,
        "C": 5,
        "E": 2
    },

    "E": {
        "C": 5,
        "D": 2
    }
}


# ---------------------------------------------------------
# DIJKSTRA'S ALGORITHM
# ---------------------------------------------------------

def dijkstra(graph, start, destination):

    # Store the shortest known distance
    # from the starting node.
    distances = {}

    # Store the previous node used to reach
    # each node in the shortest path.
    previous = {}

    # Store nodes that have not been processed yet.
    unvisited = []


    # Initialize all nodes
    for node in graph:

        distances[node] = float("inf")

        previous[node] = None

        unvisited.append(node)


    # Distance from the starting node to itself
    # is always zero.
    distances[start] = 0


    # Continue until there are no unvisited nodes
    while unvisited:

        # Find the unvisited node with the
        # smallest known distance.
        current = min(
            unvisited,
            key=lambda node: distances[node]
        )


        # Remove the current node from unvisited.
        unvisited.remove(current)


        # If we reached the destination,
        # we can stop.
        if current == destination:
            break


        # Check every neighbouring node.
        for neighbour, weight in graph[current].items():

            # Calculate the distance through
            # the current node.
            new_distance = (
                distances[current] + weight
            )


            # If this route is shorter than
            # the currently known route...
            if new_distance < distances[neighbour]:

                # Update the shortest distance.
                distances[neighbour] = new_distance

                # Remember how we reached
                # this neighbour.
                previous[neighbour] = current


    # -----------------------------------------------------
    # RECONSTRUCT THE SHORTEST PATH
    # -----------------------------------------------------

    path = []

    current = destination


    # Work backwards from the destination
    # using the previous-node information.
    while current is not None:

        path.append(current)

        current = previous[current]


    # Reverse the path so that it starts
    # at the source and ends at the destination.
    path.reverse()


    # Return both the path and total distance.
    return path, distances[destination]


# ---------------------------------------------------------
# TERMINAL TEST
# ---------------------------------------------------------

# This section runs ONLY when dijkstra.py
# is executed directly.
#
# It does NOT run when app.py imports
# the dijkstra() function.

if __name__ == "__main__":

    print()
    print(
        "Available locations:",
        ", ".join(graph.keys())
    )

    print()

    start = input(
        "Enter starting location: "
    ).upper()

    destination = input(
        "Enter destination: "
    ).upper()


    # Check whether the entered locations exist.
    if start not in graph or destination not in graph:

        print()
        print("Invalid location.")


    # Check whether source and destination
    # are the same.
    elif start == destination:

        print()
        print(
            "Starting location and destination "
            "cannot be the same."
        )


    else:

        # Run Dijkstra's algorithm.
        path, distance = dijkstra(
            graph,
            start,
            destination
        )


        print()

        print(
            "Shortest Path:",
            " -> ".join(path)
        )

        print(
            "Total Distance:",
            distance,
            "km"
        )