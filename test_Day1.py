import pytest
from Day1 import find_floor

def test_find_floor():
    assert 0 == find_floor("(())")
    assert 1 == find_floor("(()")
    assert 1 == find_floor("(())()")
