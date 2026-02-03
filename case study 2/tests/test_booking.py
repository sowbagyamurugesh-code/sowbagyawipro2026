import requests

def test_get_shows(base_url):
    res = requests.get(f"{base_url}/api/movies/101/shows")
    assert res.status_code == 200


def test_book_ticket(base_url):
    payload = {
        "movie_id": 101,
        "show_id": 1,
        "seats": 2
    }
    res = requests.post(f"{base_url}/api/bookings", json=payload)
    assert res.status_code == 201
    assert "total_price" in res.json()
