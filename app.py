from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
projects = [
    {"id": 1, "name": "Blockchain Node", "status": "Active"},
    {"id": 2, "name": "AI Model Trainer", "status": "In Progress"},
]

@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify({"projects": projects})

@app.route("/projects", methods=["POST"])
def add_project():
    new_project = request.json
    projects.append(new_project)
    return jsonify({"message": "Project added successfully", "project": new_project}), 201

ifdy>
</html== "__main__":
    app.run(debug=True)
