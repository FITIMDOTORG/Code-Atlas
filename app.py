from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/nodes")
def get_nodes():
    # Example response; integrate file parsing logic here
    return jsonify([
        {"id": "File A", "group": 1},
        {"id": "File B", "group": 1},
        {"id": "File C", "group": 2},
    ])

@app.route("/api/links")
def get_links():
    # Example response; integrate file parsing logic here
    return jsonify([
        {"source": "File A", "target": "File B"},
        {"source": "File B", "target": "File C"},
    ])

if __name__ == "__main__":
    app.run(debug=True)
