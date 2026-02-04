import requests
import pytest

def test_get_patients(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200

@pytest.mark.parametrize("payload", [
    {"name": "Arun", "age": 30, "disease": "Fever"},
    {"name": "Meena", "age": 25, "disease": "Cold"}
])
def test_add_patient(base_url, payload):
    response = requests.post(base_url, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == payload["name"]

@pytest.mark.xfail
def test_add_patient_without_name(base_url):
    response = requests.post(base_url, json={"age": 40})
    assert response.status_code == 201
@pytest.mark.skip(reason="Feature under development")
def test_update_patient(base_url):
    payload = {"age": 45}
    response = requests.put(f"{base_url}/1", json=payload)
    assert response.status_code == 200