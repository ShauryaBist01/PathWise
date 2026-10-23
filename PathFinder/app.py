from flask import Flask, render_template, request, jsonify

from dijkstra import dijkstra


app = Flask(__name__)


# Graph representing our locations and roads
graph = {
    "A": {"B": 4, "C": 3},
    "B": {"A": 4, "C": 1, "D": 2},
    "C": {"A": 3, "B": 1, "D": 5, "E": 5},
    "D": {"B": 2, "C": 5, "E": 2},
    "E": {"C": 5, "D": 2}
}


@app.route("/")
def home():

    locations = list(graph.keys())

    return render_template(
        "index.html",
        locations=locations
    )


@app.route("/find-path", methods=["POST"])
def find_path():

    data = request.get_json()

    start = data.get("start")
    destination = data.get("destination")

    # Validate locations
    if start not in graph or destination not in graph:

        return jsonify({
            "success": False,
            "message": "Invalid location."
        })


    # Find shortest path
    path, distance = dijkstra(
        graph,
        start,
        destination
    )


    return jsonify({
        "success": True,
        "path": path,
        "distance": distance
    })


if __name__ == "__main__":

    app.run(debug=True)