import pytest

def test_environment(env):
    assert env in ["dev", "stage", "prod"]
