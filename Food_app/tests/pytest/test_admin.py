import requests

BASE_URL = "http://127.0.0.1:5000/api/v1/admin"

def test_approve_restaurant():
    res = requests.put(f"{BASE_URL}/restaurants/1/approve")
    assert res.status_code in [200, 404]


def test_view_orders():
    res = requests.get(f"{BASE_URL}/orders")
    assert res.status_code == 200


def test_view_feedback():
    res = requests.get(f"{BASE_URL}/feedback")
    assert res.status_code == 200
