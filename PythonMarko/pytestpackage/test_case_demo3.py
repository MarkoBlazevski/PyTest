"""
File name should start with 'test'
Test method name should start with 'test'

py.test test_mod.py    # run tests in module

py.test somepath       # run all tests below somepath

py.test test_module.py::test_method   # only run test_method in test_module

-s to print statments
-v verbose
"""

import pytest

@pytest.yield_fixture()
def setUp():      # Can be any name not only setUp
    print("Running demo3 setUp")
    yield
    print("Running demo3 tearDown")

def test_methodA(setUp):
    print("Running demo3 method A")

def test_methodB(setUp):
    print("Running demo3 method B")
    