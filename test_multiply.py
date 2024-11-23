from main import multiply


def test_multiply():
  assert multiply(5, 4) == 20
  assert multiply(3, 4) == 12
  assert multiply (7, 0) == 0
