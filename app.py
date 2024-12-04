from flask import Flask, jsonify
from code_parser import parse_python_files

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

@app.route("/api/data")
def get_data():
    nodes, links = parse_python_files('./your_code_directory')
    data = {
        "nodes": nodes,
        "links": links
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
