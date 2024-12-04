import os

def parse_python_files(directory):
    nodes = []
    links = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                nodes.append({"id": filepath, "group": 1})
                # Fügen Sie hier die Logik hinzu, um Abhängigkeiten zu finden und Links zu erstellen

    return nodes, links
