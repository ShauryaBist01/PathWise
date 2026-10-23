async function findShortestPath() {

    const start =
        document.getElementById("start").value;

    const destination =
        document.getElementById("destination").value;


    // Reset previous route
    clearPath();


    // Source and destination cannot be the same
    if (start === destination) {

        alert(
            "Starting location and destination cannot be the same."
        );

        return;
    }


    try {

        const response = await fetch(
            "/find-path",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    start: start,

                    destination: destination

                })
            }
        );


        const data = await response.json();


        if (!data.success) {

            alert(data.message);

            return;
        }


        // Display path
        document.getElementById(
            "path-result"
        ).textContent =
            data.path.join(" → ");


        // Display distance
        document.getElementById(
            "distance-result"
        ).textContent =
            data.distance;


        // Highlight starting node
        document
            .getElementById(
                `node-${start}`
            )
            .classList.add("start");


        // Highlight destination
        document
            .getElementById(
                `node-${destination}`
            )
            .classList.add("destination");


        // Highlight nodes in path
        data.path.forEach(
            node => {

                document
                    .getElementById(
                        `node-${node}`
                    )
                    .classList.add("path");

            }
        );


        // Highlight edges
        for (
            let i = 0;
            i < data.path.length - 1;
            i++
        ) {

            const first =
                data.path[i];

            const second =
                data.path[i + 1];


            const edgeId =
                getEdgeId(
                    first,
                    second
                );


            const edge =
                document.getElementById(edgeId);


            if (edge) {

                edge.classList.add("active");

            }

        }

    }

    catch (error) {

        console.error(error);

        alert(
            "Unable to connect to the server."
        );

    }

}


/*
    Find the SVG edge between two nodes.
*/

function getEdgeId(first, second) {

    const possibleIds = [

        `edge-${first}-${second}`,

        `edge-${second}-${first}`

    ];


    for (const id of possibleIds) {

        if (
            document.getElementById(id)
        ) {

            return id;

        }

    }


    return null;
}


/*
    Clear the currently highlighted route.
*/

function clearPath() {

    // Remove node highlighting

    document
        .querySelectorAll(".node")
        .forEach(node => {

            node.classList.remove(
                "start",
                "destination",
                "path"
            );

        });


    // Remove edge highlighting

    document
        .querySelectorAll(".edges line")
        .forEach(edge => {

            edge.classList.remove(
                "active"
            );

        });


    // Reset results

    document.getElementById(
        "path-result"
    ).textContent = "—";


    document.getElementById(
        "distance-result"
    ).textContent = "—";

}


/*
    Reset the entire graph.
*/

function resetGraph() {

    clearPath();

}