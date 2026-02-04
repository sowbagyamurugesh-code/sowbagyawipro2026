from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "patients.json"


# Load patients from JSON file
def load_patients():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


# Save patients to JSON file
def save_patients(patients):
    with open(DATA_FILE, "w") as file:
        json.dump(patients, file, indent=4)


# GET all patients
@app.route("/api/patients", methods=["GET"])
def get_patients():
    patients = load_patients()
    return jsonify(patients), 200


# POST add new patient
@app.route("/api/patients", methods=["POST"])
def add_patient():
    patients = load_patients()
    data = request.get_json()

    if not data.get("name"):
        return jsonify({"error": "Patient name is required"}), 400

    new_id = patients[-1]["id"] + 1 if patients else 1

    new_patient = {
        "id": new_id,
        "name": data.get("name"),
        "age": data.get("age"),
        "gender": data.get("gender"),
        "contact": data.get("contact"),
        "disease": data.get("disease"),
        "doctor": data.get("doctor")
    }

    patients.append(new_patient)
    save_patients(patients)

    return jsonify(new_patient), 201


# GET patient by ID
@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    patients = load_patients()

    for patient in patients:
        if patient["id"] == pid:
            return jsonify(patient), 200

    return jsonify({"error": "Patient not found"}), 404


# PUT update patient
@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    patients = load_patients()
    data = request.get_json()

    for patient in patients:
        if patient["id"] == pid:
            patient["name"] = data.get("name", patient["name"])
            patient["age"] = data.get("age", patient["age"])
            patient["gender"] = data.get("gender", patient["gender"])
            patient["contact"] = data.get("contact", patient["contact"])
            patient["disease"] = data.get("disease", patient["disease"])
            patient["doctor"] = data.get("doctor", patient["doctor"])

            save_patients(patients)
            return jsonify(patient), 200

    return jsonify({"error": "Patient not found"}), 404


# DELETE patient
@app.route("/api/patients/<int:pid>", methods=["DELETE"])
def delete_patient(pid):
    patients = load_patients()

    for patient in patients:
        if patient["id"] == pid:
            patients.remove(patient)
            save_patients(patients)
            return jsonify({"message": "Patient deleted successfully"}), 200

    return jsonify({"error": "Patient not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
