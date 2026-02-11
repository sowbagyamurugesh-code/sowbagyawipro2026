import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

def test_add_dish():
    payload = {
        "name": "Pizza",
        "type": "Fast Food",
        "price": 120,
        "available_time": "Night",
        "image": "pizza.png"
    }

    res = requests.post(f"{BASE_URL}/restaurants/1/dishes", json=payload)
    assert res.status_code in [201, 400]
