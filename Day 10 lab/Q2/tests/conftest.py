import pytest

# ---------- MODULE SCOPE FIXTURE ----------
@pytest.fixture(scope="module")
def numbers():
    print("\n[SETUP] numbers fixture (module scope)")
    data = (10, 5)
    yield data
    print("\n[TEARDOWN] numbers fixture (module scope)")


# ---------- FUNCTION SCOPE FIXTURE ----------
@pytest.fixture(scope="function")
def empty_list():
    print("\n[SETUP] empty_list fixture (function scope)")
    lst = []
    yield lst
    print("\n[TEARDOWN] empty_list fixture (function scope)")
