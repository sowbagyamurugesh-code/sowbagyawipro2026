import pytest
from Day11.auth import login

@pytest.mark.smoke
def test_valid_login():
    assert login("admin", "admin123") == "Login Successful"
def test_invalid_login():
    assert login("user", "wrong") == "Invalid Credentials"