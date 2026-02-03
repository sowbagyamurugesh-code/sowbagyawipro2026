import requests

def test_get_movies(base_url):
    res = requests.get(f"{base_url}/api/movies")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_add_movie(base_url):
    payload = {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 300
    }
    res = requests.post(f"{base_url}/api/movies", json=payload)
    assert res.status_code == 201
