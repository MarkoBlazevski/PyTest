import pytest

@pytest.yield_fixture()
def setUp():      # Can be any name not only setUp
    print("Once before every method")
    yield
    print("Once after every method")
def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")