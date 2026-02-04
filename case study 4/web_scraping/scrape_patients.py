import requests
from bs4 import BeautifulSoup

response = requests.get("http://127.0.0.1:5000/api/patients")
patients = response.json()

for p in patients:
    print(p["name"], p["age"], p["disease"], p.get("doctor"))
