import pytest
from main import hello


def test_hello():
  x = hello()
  assert x == 'hello'
